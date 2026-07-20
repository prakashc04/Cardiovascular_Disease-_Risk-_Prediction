
# ❤️ Cardiovascular Disease Prediction using Machine Learning

## 📌 Project Overview

This project predicts the risk of cardiovascular disease using Machine Learning algorithms based on patient health records. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, a Flask web application for prediction, and a Power BI dashboard for interactive visualization.

---

## 🎯 Objectives

- Predict cardiovascular disease risk.
- Perform data cleaning and preprocessing.
- Analyze patient health data using EDA.
- Compare multiple Machine Learning models.
- Deploy the best model using Flask.
- Build an interactive Power BI dashboard.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Flask
- Joblib
- Jupyter Notebook
- Power BI

---

## 📂 Project Structure

```text
cardiovascular-disease-prediction/
│── cardio.ipynb
│── app.py
│── xgb_cardiovascular_model.pkl
│── requirements.txt
│── README.md
│── Cardiovascular_Dashboard.pbix
│
└── images/
    ├── roc_curve.png
    ├── model_performance_comparison.png
    ├── correlation_heatmap.png
    ├── numerical_features_distribution.png
    ├── outlier_detection_bp_bmi.png
    ├── cholesterol_vs_cardiovascular_disease.png
    ├── pairplot_health_features.png
    ├── bmi_vs_cardiovascular_risk.png
    ├── blood_pressure_vs_cardiovascular_risk.png
    ├── age_distribution_by_risk.png
    └── target_variable_distribution.png
```

---

## 📊 Dataset Features

- Age
- Gender
- Height
- Weight
- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol
- Glucose
- Smoking
- Alcohol Consumption
- Physical Activity
- BMI (Feature Engineered)
- Pulse Pressure
- Mean Arterial Pressure

---

## 🤖 Machine Learning Models

- Logistic Regression
- Random Forest
- XGBoost (Best Performing Model)

---

## 📈 Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

---

# 📷 Visualizations

### 1. Receiver Operating Characteristic (ROC) Curve

Evaluates model performance using ROC-AUC.

### 2. Model Performance Comparison

Comparison of Accuracy, Precision, Recall, and F1-Score.

### 3. Correlation Heatmap

Shows relationships between all features.

### 4. Distribution of Numerical Features

Distribution of Age, Blood Pressure, and BMI.

### 5. Outlier Detection in Blood Pressure and BMI

Identifies outliers using Box Plots.

### 6. Cholesterol Levels vs Cardiovascular Disease

Analyzes the effect of cholesterol on cardiovascular disease.

### 7. Pair Plot of Health Features

Visualizes pairwise relationships among important variables.

### 8. BMI vs Cardiovascular Risk

Compares BMI distributions between patients with and without cardiovascular disease.

### 9. Systolic vs Diastolic Blood Pressure by Cardiovascular Risk

Scatter plot illustrating blood pressure patterns.

### 10. Age Distribution by Cardiovascular Risk

Shows age distribution across cardiovascular risk groups.

### 11. Target Variable Distribution

Displays the distribution of cardiovascular disease classes.

---

## 💻 Flask Web Application

The Flask application allows users to enter patient health information and predicts whether the patient is at high cardiovascular risk.

Prediction Output:

- ✅ No Cardiovascular Risk
- ⚠️ High Cardiovascular Risk

---

## 📊 Power BI Dashboard

Interactive dashboard includes:

- Age Analysis
- BMI Analysis
- Blood Pressure Analysis
- Cholesterol Analysis
- Cardiovascular Risk Distribution
- Interactive Filters

---

## 🚀 Future Improvements

- Hyperparameter tuning
- Deep Learning models
- Streamlit deployment
- Cloud deployment
- Real-time prediction API

---

## 👨‍💻 Author

**prakash kumar**

- GitHub: https://github.com/prakashc04
- LinkedIn: www.linkedin.com/in/
prakash-kumar-b733463a7

---

⭐ If you found this project useful, please consider giving it a star.
