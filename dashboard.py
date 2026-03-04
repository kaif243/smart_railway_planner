import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
from utils.recommendation import coach_recommendation

st.set_page_config(page_title="Smart Railway Planner", layout="wide")

st.title("🚆 Smart Railway Resource Planning System")
st.write("Data-Driven Decision Support for Railway Resource Allocation")

# -------------------------
# Load Dataset
# -------------------------

data_path = os.path.join(os.path.dirname(__file__), "..", "data", "railway_data.csv")
df = pd.read_csv(data_path)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# -------------------------
# Passenger Demand by Route
# -------------------------

st.subheader("🚉 Passenger Demand by Route")

route_demand = df.groupby(
["Source","Destination"]
)["Passenger_Count"].mean().reset_index()

fig = px.bar(
route_demand,
x="Source",
y="Passenger_Count",
color="Destination",
title="Average Passenger Demand by Route"
)

st.plotly_chart(fig,use_container_width=True)

# -------------------------
# Hourly Demand
# -------------------------

st.subheader("⏰ Passenger Demand by Hour")

hour_demand = df.groupby("Hour")["Passenger_Count"].mean().reset_index()

fig2 = px.line(
hour_demand,
x="Hour",
y="Passenger_Count",
title="Passenger Demand Across Hours"
)

st.plotly_chart(fig2,use_container_width=True)

# -------------------------
# Peak Travel Hour
# -------------------------

peak_hour = df.groupby("Hour")["Passenger_Count"].mean().idxmax()

st.info(f"🔥 Peak Travel Hour Detected: {peak_hour}:00")

# -------------------------
# Platform Congestion
# -------------------------

st.subheader("🚉 Platform Usage Analysis")

platform_usage = df.groupby("Platform")["Passenger_Count"].sum().reset_index()

fig3 = px.bar(
platform_usage,
x="Platform",
y="Passenger_Count",
title="Passenger Load by Platform"
)

st.plotly_chart(fig3,use_container_width=True)

# -------------------------
# Route Demand Heatmap
# -------------------------

st.subheader("🗺 Route Demand Heatmap")

pivot = df.pivot_table(
values="Passenger_Count",
index="Source",
columns="Destination",
aggfunc="mean"
)

fig4 = px.imshow(
pivot,
title="Railway Route Demand Heatmap"
)

st.plotly_chart(fig4,use_container_width=True)

# -------------------------
# Prediction Section
# -------------------------

st.subheader("🤖 Predict Passenger Demand")

col1,col2,col3 = st.columns(3)

with col1:
    hour = st.slider("Travel Hour",0,23,10)

with col2:
    capacity = st.selectbox("Seat Capacity",[500,600,700,800])

with col3:
    coaches = st.slider("Number of Coaches",5,20,10)

col4,col5,col6 = st.columns(3)

with col4:
    platform = st.slider("Platform Number",1,12,3)

with col5:
    weekend = st.selectbox("Weekend",[0,1])

with col6:
    holiday = st.selectbox("Holiday",[0,1])

# -------------------------
# Prediction Button
# -------------------------

if st.button("Predict Demand"):

    features = pd.DataFrame({
        "Hour":[hour],
        "Seat_Capacity":[capacity],
        "Number_of_Coaches":[coaches],
        "Platform":[platform],
        "Weekend":[weekend],
        "Holiday":[holiday]
    })

    prediction = model.predict(features)[0]

    st.metric("🚶 Predicted Passengers", int(prediction))
    st.write("🪑 Train Capacity:", capacity)

    # Crowd Pressure Index
    cpi = prediction / capacity
    st.metric("📊 Crowd Pressure Index (CPI)", round(cpi,2))

    if cpi > 1:
        st.error("⚠ Severe overcrowding expected")

    elif cpi > 0.8:
        st.warning("⚠ Train may become crowded")

    else:
        st.success("✅ Capacity is sufficient")

    # Recommendation
    recommendation = coach_recommendation(prediction,capacity)

    st.info("🚆 Recommendation: " + recommendation)

# -------------------------
# Delay Analysis
# -------------------------

st.subheader("⏳ Delay Impact Analysis")

fig5 = px.scatter(
df,
x="Delay_Minutes",
y="Passenger_Count",
title="Delay vs Passenger Load"
)

st.plotly_chart(fig5,use_container_width=True)

# -------------------------
# Footer
# -------------------------

st.markdown("---")

st.markdown(
"""
Smart Railway Resource Planning System  
Hackathon Project – Data Driven Railway Optimization
"""
)