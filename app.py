from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load your trained model
model = joblib.load("xgb_cardiovascular_model.pkl")

# Preprocess user input (feature engineering)
def preprocess_user_input(data):
    df = pd.DataFrame([data])
    df['bmi'] = df['weight'] / ((df['height']/100)**2)
    df['pulse_pressure'] = df['ap_hi'] - df['ap_lo']
    df['htn_flag'] = ((df['ap_hi'] >= 140) | (df['ap_lo'] >= 90)).astype(int)
    return df

# Determine risk & prescription
def get_prescription(prob):
    if prob > 0.7:
        return "High Risk", "Consult cardiologist immediately, adopt low-salt diet and exercise.", "high"
    elif prob > 0.4:
        return "Low Risk", " Maintain lifestyle, monitor blood pressure regularly.", "low"
    else:
        return "No Cardio", " You are fit & fine! Keep a healthy lifestyle.", "no"

# Home page
@app.route("/")
def home():
    return render_template("template.html")

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = preprocess_user_input(data)
    prob = model.predict_proba(df)[0][1]
    risk, prescription, css_class = get_prescription(prob)
    return jsonify({"risk": risk, "prescription": prescription, "class": css_class})

if __name__ == "__main__":
    app.run(debug=True)
