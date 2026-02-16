import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

def predict_message(message):
    message_vec = vectorizer.transform([message])
    
    prediction = model.predict(message_vec)[0]
    probabilities = model.predict_proba(message_vec)[0]

    max_prob = max(probabilities)

    if prediction == "ham":
        severity = "low"
    elif prediction == "spam":
        severity = "medium"
    else:
        severity = "high"

    return {
        "classification": prediction,
        "risk_score": round(float(max_prob), 2),
        "severity": severity
    }




