import joblib
import os

# Caminhos absolutos (funciona local + Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):

    X = vectorizer.transform([message])
    probabilities = model.predict_proba(X)[0]
    predicted_class = model.predict(X)[0]

    # Probabilidade máxima
    confidence = max(probabilities)

    # Converter para percentagem
    risk_score = int(confidence * 100)

    # 🔥 Garantir limite 0–100 (versão segura)
    risk_score = max(0, min(100, risk_score))

    # Definir nível de risco baseado na classificação
    if predicted_class == "Phishing":
        risk_level = "high"
    elif predicted_class == "Spam":
        risk_level = "medium"
    else:
        risk_level = "low"

    return {
        "classification": predicted_class,
        "risk_score": risk_score,
        "risk_level": risk_level
    }







