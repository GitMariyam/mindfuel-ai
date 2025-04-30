# app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/fact")
def get_fact():
    return jsonify({"fact": "This is a placeholder MindFuel tip."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

