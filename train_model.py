import os
import argparse
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

COMMON_VIB = ["vibration","vib","vibration_mm_s"]
COMMON_TEMP = ["temperature","temp","temp_c"]
COMMON_CURR = ["current","motor_current","amps"]
COMMON_LABEL = ["label","status","health","class"]

def detect_column(cols, candidates):
    for c in candidates:
        for col in cols:
            if c.lower() == col.lower():
                return col
    for c in candidates:
        for col in cols:
            if c.lower() in col.lower():
                return col
    return None

def load_and_prepare(path):
    df = pd.read_csv(path)
    cols = df.columns.tolist()

    vib = detect_column(cols, COMMON_VIB)
    temp = detect_column(cols, COMMON_TEMP)
    curr = detect_column(cols, COMMON_CURR)
    label = detect_column(cols, COMMON_LABEL)

    if vib is None or temp is None or curr is None:
        raise ValueError("Could not detect vibration/temp/current columns")

    X = df[[vib, temp, curr]]
    X.columns = ["vibration","temperature","current"]
    X = X.fillna(X.median())

    if label is None:
        y = []
        for _,r in X.iterrows():
            score=0
            if r.vibration>6: score+=1
            if r.temperature>70: score+=1
            if r.current>12: score+=1
            if score>=2: y.append("CRITICAL")
            elif score==1: y.append("WARNING")
            else: y.append("HEALTHY")
        y = pd.Series(y)
    else:
        y = df[label].astype(str).str.upper()
        y = y.replace({
            "OK":"HEALTHY",
            "GOOD":"HEALTHY",
            "BAD":"CRITICAL",
            "FAIL":"CRITICAL"
        })

    return X, y

def train(csv_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    X, y = load_and_prepare(csv_path)

    label_map = {"HEALTHY":0,"WARNING":1,"CRITICAL":2}
    y_enc = y.map(label_map)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_enc, test_size=0.2, random_state=42, stratify=y_enc
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train_s, y_train)

    print("TRAINING COMPLETE")
    print(classification_report(y_test, model.predict(X_test_s)))

    joblib.dump(model, f"{out_dir}/pump_model.pkl")
    joblib.dump(scaler, f"{out_dir}/scaler.pkl")
    
    json.dump({
        "features":["vibration","temperature","current"],
        "label_map": label_map
    }, open(f"{out_dir}/feature_meta.json","w"), indent=2)

    print("Saved model to:", out_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--out", default="model")
    args = parser.parse_args()
    train(args.csv, args.out)
