# 🚆 Smart Railway Resource Planning System

## 📌 Project Overview

Railway networks manage thousands of trains, platforms, and passengers daily. Manual planning often leads to overcrowding, inefficient resource allocation, and delays.

The **Smart Railway Resource Planning System** is a data-driven application that analyzes railway operational data to help planners make smarter decisions regarding train scheduling, coach allocation, and platform usage.

This system uses **data analysis, visualization, and machine learning** to predict passenger demand and recommend optimal railway resource allocation.

---

# 🎯 Objectives

The goal of this project is to:

* Predict passenger demand across railway routes
* Identify peak travel periods
* Detect overcrowding risks
* Recommend additional coaches when needed
* Analyze platform congestion
* Provide data-driven insights for railway planners

---

# 🧠 Key Features

## 1️⃣ Passenger Demand Prediction

A **Machine Learning model (Random Forest)** predicts the number of passengers for a given train configuration.

Inputs include:

* Travel hour
* Seat capacity
* Number of coaches
* Platform number
* Weekend indicator
* Holiday indicator

---

## 2️⃣ Crowd Pressure Index (CPI)

The system calculates a **Crowd Pressure Index**:

CPI = Predicted Passengers / Seat Capacity

This helps planners quickly understand whether a train will be:

| CPI Value | Status          |
| --------- | --------------- |
| < 0.8     | Low demand      |
| 0.8 – 1.0 | Moderate demand |
| > 1.0     | Overcrowded     |

---

## 3️⃣ Smart Coach Recommendation

If predicted passengers exceed train capacity, the system recommends **additional coaches** to reduce overcrowding.

Example:

Predicted passengers: 720
Train capacity: 600

Recommendation: Add extra coaches.

---

## 4️⃣ Passenger Demand Visualization

Interactive charts help planners understand travel patterns:

* Passenger demand by route
* Hourly passenger demand trends
* Platform usage analysis
* Delay impact analysis

---

## 5️⃣ Peak Travel Window Detection

The system automatically identifies **peak travel hours** when passenger demand is highest.

This allows planners to schedule **additional trains or coaches during peak periods**.

---

## 6️⃣ Route Demand Heatmap

A heatmap visualization shows which **source-destination routes** experience the highest passenger demand.

This helps railway planners prioritize high-demand routes.

---

# 📊 Dataset

The dataset used in this project is **synthetically generated** to simulate real railway operations.

Example dataset fields:

| Column            | Description             |
| ----------------- | ----------------------- |
| Train_ID          | Unique train identifier |
| Source            | Departure city          |
| Destination       | Arrival city            |
| Hour              | Travel time             |
| Passenger_Count   | Number of passengers    |
| Seat_Capacity     | Available seats         |
| Number_of_Coaches | Total train coaches     |
| Platform          | Assigned platform       |
| Delay_Minutes     | Train delay             |
| Weekend           | Weekend indicator       |
| Holiday           | Holiday indicator       |

Synthetic data was generated to simulate realistic railway travel patterns across multiple Indian cities.

---

# ⚙️ Technology Stack

**Programming Language**

Python

**Libraries Used**

* Pandas
* NumPy
* Scikit-learn
* Plotly
* Streamlit

**Machine Learning Model**

Random Forest Regressor

---

# 📁 Project Structure

```
hackthon-railway
│
├── app
│   └── dashboard.py
│
├── data
│   └── railway_data.csv
│
├── models
│   ├── model.pkl
│   └── train_model.py
│
├── utils
│   ├── data_generator.py
│   └── recommendation.py
│
├── requirements.txt
│
└── README.md
```

---

# ▶️ How to Run the Project

## 1️⃣ Clone the Repository

```
git clone <repository-link>
cd hackthon-railway
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Generate Dataset

```
python utils/data_generator.py
```

---

## 4️⃣ Train the Model

```
python models/train_model.py
```

---

## 5️⃣ Run the Dashboard

```
streamlit run app/dashboard.py
```

Then open:

```
http://localhost:8501
```

---

# 📈 Expected Output

The dashboard provides:

* Passenger demand analytics
* Route demand heatmap
* Platform usage insights
* Peak travel hour detection
* Passenger demand prediction
* Smart coach allocation recommendations

---

# 🏆 Hackathon Focus

This project demonstrates:

* Practical data-driven decision making
* Machine learning application in transportation planning
* Interactive data visualization
* Smart railway resource optimization

---

# 📌 Future Improvements

Potential future enhancements include:

* Real-time railway data integration
* Advanced time-series demand forecasting
* Train scheduling optimization
* Railway network visualization on maps
* Deep learning based demand prediction

---

# 👨‍💻 Author

**Kaif Shaik**

CVR College of Engineering

Machine Learning & Data Analytics Enthusiast
