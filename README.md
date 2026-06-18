<div align="center">

# 🛠⚡ PumpGuard AI

### AI-Powered Industrial Pump Health Prediction System

Predict pump failures before they happen using Machine Learning and real-time sensor readings.

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-Web_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Machine_Learning-Random_Forest-10B981?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Industrial_AI-Predictive_Maintenance-orange?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Scikit--Learn-ML_Model-F7931E?style=for-the-badge"/>
</p>

### 🔮 Predict • Detect • Prevent • Maintain

</div>

---

# ✨ Overview

PumpGuard AI is a Machine Learning-powered predictive maintenance system designed to monitor industrial pump health using only three critical operating parameters:

⚙️ Vibration (mm/s)

🌡 Temperature (°C)

⚡ Motor Current (A)

The system intelligently predicts the operational status of a pump and helps engineers identify risks before failures occur.

---

# 🎯 Pump Health Classification

PumpGuard AI classifies pumps into:

🟢 **HEALTHY**

🟠 **WARNING**

🔴 **CRITICAL**

and provides:

✅ Failure Risk Score

✅ Maintenance Recommendations

✅ Predictive Maintenance Insights

✅ Real-Time Decision Support

---

# 🚀 Key Features

### 🧠 Machine Learning Prediction

* Random Forest Classification
* Real-Time Pump Assessment
* Predictive Failure Detection
* Multi-Parameter Analysis

### 📊 Smart Monitoring

* Vibration Analysis
* Temperature Monitoring
* Current Consumption Tracking
* Health Score Calculation

### 🛠 Maintenance Intelligence

* Repair Recommendations
* Failure Risk Assessment
* Preventive Maintenance Guidance
* Operational Health Insights

### 🌐 Deployment Ready

* Streamlit Dashboard
* Lightweight Architecture
* Offline Compatible
* No External APIs

---

# 📸 Dashboard Preview

### Pump Health Analysis

```text
Pump Status: WARNING

Failure Risk: 68%

Recommendation:
Inspect bearing condition and vibration levels.
```

### Critical Alert Example

```text
Pump Status: CRITICAL

Failure Risk: 92%

Recommendation:
Immediate maintenance required.
Potential motor or bearing failure detected.
```

---

# 🏗 Project Structure

```text
PumpGuard-AI/
│
├── app.py
├── train_model.py
├── requirements.txt
│
├── data/
│   └── pumphealth.csv
│
├── model/
│   ├── pump_model.pkl
│   ├── scaler.pkl
│   └── feature_meta.json
│
└── README.md
```

---

# ⚙️ Technologies Used

| Category         | Technologies             |
| ---------------- | ------------------------ |
| Frontend         | Streamlit                |
| Machine Learning | Scikit-Learn             |
| Data Processing  | Pandas, NumPy            |
| Model Storage    | Joblib                   |
| Algorithm        | Random Forest Classifier |
| Language         | Python                   |

---

# 🧠 How It Works

### Step 1 — Train Model

The system learns from historical pump sensor data:

* Vibration
* Temperature
* Motor Current

```bash
python train_model.py --csv data/pumphealth.csv --out model
```

Generated Artifacts:

```text
model/
├── pump_model.pkl
├── scaler.pkl
└── feature_meta.json
```

---

### Step 2 — Launch Dashboard

```bash
streamlit run app.py
```

Enter:

* Vibration
* Temperature
* Current

Get:

* Health Prediction
* Risk Score
* Maintenance Recommendations

---

# 📦 Installation

### Clone Repository

```bash
git clone https://github.com/chandramouli9392/PumpGuard-AI.git
cd PumpGuard-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Required Libraries:

```text
streamlit
scikit-learn
pandas
numpy
joblib
```

---

# ☁️ Deployment

### Streamlit Cloud

1. Push project to GitHub
2. Login to Streamlit Cloud
3. Select repository
4. Choose:

```text
app.py
```

5. Click Deploy 🚀

---

# 📈 Why PumpGuard AI?

### Business Benefits

💰 Reduce Maintenance Costs

⚙️ Improve Equipment Reliability

📉 Reduce Downtime

🛠 Enable Predictive Maintenance

🏭 Improve Industrial Productivity

🧠 AI-Powered Decision Making

---

# 🔮 Future Roadmap

* [ ] Deep Learning Models
* [ ] Real-Time IoT Integration
* [ ] MQTT Sensor Streaming
* [ ] Dashboard Analytics
* [ ] Multi-Pump Monitoring
* [ ] Failure Trend Forecasting
* [ ] Mobile Application
* [ ] Cloud Monitoring Platform

---

# 👨‍💻 Developer

### Boppana Chandramouli

AI Engineer • Machine Learning Enthusiast • Industrial AI Developer

GitHub:
https://github.com/chandramouli9392

---

<div align="center">

### ⭐ Star this repository if you found it useful

Built with ❤️ using Python, Streamlit, Scikit-Learn & Predictive Maintenance AI

</div>
