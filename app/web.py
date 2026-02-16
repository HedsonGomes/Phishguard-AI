from flask import Flask, render_template, request
from app.detector import predict_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            prediction = predict_message(message)

            # Probabilidade real de phishing
            phishing_probability = prediction["phishing_probability"]

            risk_score = round(phishing_probability * 100)

            # 🔥 Calibração do risco
            if risk_score < 35:
                risk_level = "low"
                classification = "Legítimo"
            elif risk_score < 65:
                risk_level = "medium"
                classification = "Spam"
            else:
                risk_level = "high"
                classification = "Phishing"

            result = {
                "classification": classification,
                "risk_score": risk_score,
                "risk_level": risk_level
            }

    return render_template("index.html", result=result, message=message)


if __name__ == "__main__":
    app.run(debug=True)

