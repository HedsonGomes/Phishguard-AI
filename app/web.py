from flask import Flask, render_template, request
from app.detector import predict_message

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    message = ""

    if request.method == "POST":
        message = request.form["message"]
        result = predict_message(message)

    return render_template("index.html", result=result, message=message)

if __name__ == "__main__":
    app.run()
