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

            phishing_prob = prediction["phishing_probability"]
            spam_prob = prediction["spam_probability"]
            total_risk = prediction["total_risk"]

            risk_percent = round(total_risk * 100)

            # 🎯 CLASSIFICAÇÃO FINAL
            if phishing_prob > 0.50:
                classification = "Phishing"
                risk_level = "high"

            elif total_risk > 0.50:
                classification = "Spam"
                risk_level = "medium"

            else:
                classification = "Legítimo"
                risk_level = "low"

            result = {
                "classification": classification,
                "risk_score": risk_percent,
                "risk_level": risk_level
            }

    return render_template("index.html", result=result, message=message)


if __name__ == "__main__":
    app.run(debug=True)


