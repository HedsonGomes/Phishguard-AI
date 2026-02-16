import joblib
import os

# Caminhos absolutos para funcionar em produção (Render)
BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):
    X = vectorizer.transform([message])

    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    # Classes do modelo (ordem importante!)
    classes = model.classes_

    # Probabilidade de phishing
    phishing_probability = 0.0

    if "phishing" in classes:
        phishing_index = list(classes).index("phishing")
        phishing_probability = probabilities[phishing_index]

    # Converter nomes para versão bonita
    if prediction == "ham":
        classification = "Legítimo"
    elif prediction == "spam":
        classification = "Spam"
    else:
        classification = "Phishing"

    return {
        "classification": classification,
        "phishing_probability": float(phishing_probability)
    }







