import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample training data
X = np.array([
    [2, 60, 55],
    [3, 65, 60],
    [4, 70, 65],
    [5, 75, 70],
    [6, 80, 75],
    [7, 85, 80],
    [8, 90, 85],
    [9, 95, 90]
])

y = np.array([50, 55, 60, 65, 70, 76, 82, 88])

# Train model
model = LinearRegression()
model.fit(X, y)

# App title
st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final score using study hours, attendance, and previous score.")

# User inputs
study_hours = st.slider("Study Hours per Week", 1, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous_score = st.slider("Previous Score", 0, 100, 70)

# Prediction button
if st.button("Predict Final Score"):
    input_data = np.array([[study_hours, attendance, previous_score]])
    prediction = model.predict(input_data)[0]

    prediction = max(0, min(100, prediction))

    st.success(f"Predicted Final Score: {prediction:.2f}")