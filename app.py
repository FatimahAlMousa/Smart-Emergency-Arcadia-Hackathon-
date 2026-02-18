from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder=None)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def analyze_data(data):
    heart = float(data.get("heart", 0))
    pressure = float(data.get("pressure", 0))
    oxygen = float(data.get("oxygen", 0))
    temp = float(data.get("temperature", 0))

    if oxygen < 90 or heart > 130 or pressure > 180 or temp > 40:
        return "🚨 Emergency! Ambulance has been called."

    if heart < 60 or heart > 100 or pressure > 140 or temp > 38:
        return "⚠️ Needs medical follow-up."

    return "✅ Normal condition."

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "AI Hackathon.html")


@app.route('/<path:path>')
def serve_files(path):
    return send_from_directory(BASE_DIR, path)

@app.route("/analyze", methods=["POST"])
def analyze():
    result = analyze_data(request.form)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
