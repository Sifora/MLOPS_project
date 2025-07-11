from flask import Flask, request, jsonify
from Model import predict  # Import the predict function from model.py

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask app is running!"

@app.route("/predict", methods=["POST"])

def predict_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    prediction = predict(text)
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(debug=True)
