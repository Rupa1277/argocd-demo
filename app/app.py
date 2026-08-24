from flask import Flask, jsonify

app = Flask(__name__)

FEATURES = ["Homepage"]

@app.route("/")
def home():
    return f"<h1>Feature Tracker App</h1><p>Active features: {', '.join(FEATURES)}</p>"

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)