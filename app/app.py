from flask import Flask
# CI/CD demo application
app = Flask(__name__)

@app.route("/")
def hello():
    return "changes made to Version 1 - deployed via Argo CD! To check"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)