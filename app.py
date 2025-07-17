from flask import Flask, request, jsonify
from prometheus_client import Counter, Summary, generate_latest

from Model import predict

REQUEST_COUNT = Counter("request_count", "Total prediction requests")
INFERENCE_TIME = Summary("inference_processing_seconds", "Time spent processing prediction")


app = Flask(__name__)


@app.route("/")
def home():
    return "Flask app is running!"

@app.route("/predict", methods=["POST"])
@INFERENCE_TIME.time()

def predict_route():
    REQUEST_COUNT.inc()
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = predict(text)
    return jsonify(prediction)

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(debug=True)
