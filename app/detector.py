import joblib
import os

# Caminhos absolutos
BASE_DIR = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):

    X = vectorizer.transform([message])
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    # Criar dicionário classe → probabilidade
    prob_dict = dict(zip(classes, probabilities))

    # 🔥 RISCO BASEADO APENAS NA PROBABILIDADE DE PHISHING
    phishing_probability = prob_dict.get("phishing", 0)

    risk_score = int(phishing_probability * 100)

    # Garantir limites
    risk_score = max(0, min(100, risk_score))

    # Determinar nível de risco
    if risk_score >= 60:
        risk_level = "high"
    elif risk_score >= 30:
        risk_level = "medium"
    else:
        risk_level = "low"

    # Classificação textual bonita
    predicted_class = model.predict(X)[0]

    if predicted_class == "ham":
        classification = "Legítimo"
    elif predicted_class == "spam":
        classification = "Spam"
    else:
        classification = "Phishing"

    return {
        "classification": classification,
        "risk_score": risk_score,
        "risk_level": risk_level
    }







