import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):

    X = vectorizer.transform([message])
    probs = model.predict_proba(X)[0]

    classes = model.classes_

    prob_dict = dict(zip(classes, probs))

    # 🔥 Probabilidade específica de phishing
    phishing_prob = prob_dict.get("phishing", 0)

    # 🎯 Classificação final do modelo
    predicted_class = model.predict(X)[0]

    # 🔥 Risk score baseado APENAS no phishing
    risk_score = round(phishing_prob * 100)

    # 🎨 Definir nível visual com base na probabilidade de phishing
    if phishing_prob > 0.6:
        risk_level = "high"
    elif phishing_prob > 0.3:
        risk_level = "medium"
    else:
        risk_level = "low"

    # 📘 Texto amigável
    label_map = {
        "ham": "Legítimo",
        "spam": "Spam",
        "phishing": "Phishing"
    }

    return {
        "classification": label_map.get(predicted_class, predicted_class),
        "risk_score": risk_score,
        "risk_level": risk_level
    }






