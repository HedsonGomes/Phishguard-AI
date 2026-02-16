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

        raw_class = prediction["classification"]
        risk_score = prediction["risk_score"]

        # Converter para percentagem
        risk_percent = round(risk_score * 100)

        # 🎯 Mapear labels internas para visíveis
        if raw_class == "ham":
            classification = "Legítimo"
            severity = "low"
            advice = "Mensagem legítima. Nenhuma ação necessária."

        elif raw_class == "spam":
            classification = "Spam"
            severity = "medium"
            advice = "Mensagem suspeita. Analise antes de agir."

        elif raw_class == "phishing":
            classification = "Phishing"
            severity = "high"
            advice = "Alto risco de phishing. Não clique em links nem forneça dados."

        result = {
            "classification": classification,
            "risk_score": risk_percent,
            "severity": severity,
            "advice": advice
        }

    return render_template("index.html", result=result, message=message)


if __name__ == "__main__":
    app.run(debug=True)

