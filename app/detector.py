import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_message(message):

    X = vectorizer.transform([message])
    probabilities = model.predict_proba(X)[0]
    classes = model.classes_

    prob_dict = dict(zip(classes, probabilities))

    ham_prob = prob_dict.get("ham", 0)
    spam_prob = prob_dict.get("spam", 0)
    phishing_prob = prob_dict.get("phishing", 0)

    # 🔥 RISCO GLOBAL = Spam + Phishing
    total_risk = spam_prob + phishing_prob

    return {
        "ham_probability": float(ham_prob),
        "spam_probability": float(spam_prob),
        "phishing_probability": float(phishing_prob),
        "total_risk": float(total_risk)
    }






