from flask import Flask, render_template, request
from app.detector import predict_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        message = request.form["message"]

        prediction = predict_message(message)

        classification = prediction["classification"]
        phishing_probability = prediction["phishing_probability"]

        # 🔥 Risk base real
        base_score = int(phishing_probability * 100)

        # 🔥 Calibração profissional por classe
        if classification == "Phishing":
            risk_score = max(70, base_score)
            risk_level = "high"

        elif classification == "Spam":
            risk_score = max(40, min(base_score, 60))
            risk_level = "medium"

        else:  # Legítimo
            risk_score = min(base_score, 30)
            risk_level = "low"

        # 🔥 Segurança extra
        risk_score = max(0, min(100, risk_score))

        result = {
            "classification": classification,
            "risk_score": risk_score,
            "risk_level": risk_level
        }

    return render_template("index.html", result=result, message=message)


if __name__ == "__main__":
    app.run()



