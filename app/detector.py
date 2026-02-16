import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):

    X = vectorizer.transform([message])

    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    # Criar dicionário com probabilidades reais
    prob_dict = dict(zip(classes, probabilities))

    phishing_probability = prob_dict.get("phishing", 0)

    return {
        "phishing_probability": float(phishing_probability)
    }




