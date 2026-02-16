import joblib
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):
    X = vectorizer.transform([message])
    probabilities = model.predict_proba(X)[0]
    prediction = model.classes_[probabilities.argmax()]
    risk_score = max(probabilities)

    return {
        "classification": prediction,  # ham / spam / phishing
        "risk_score": round(float(risk_score), 4)
    }






