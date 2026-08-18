from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps CI/CD Pipeline Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 80px;
                background-color: #f4f6f9;
            }

            .container {
                background: white;
                padding: 40px;
                margin: auto;
                width: 70%;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.15);
            }

            h1 {
                color: #2c3e50;
            }

            .version {
                font-size: 28px;
                font-weight: bold;
                margin: 20px;
            }

            .success {
                color: green;
                font-size: 22px;
            }

            .pipeline {
                margin-top: 30px;
                font-size: 20px;
                line-height: 2;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 DevOps CI/CD Pipeline Demo</h1>

            <div class="version">
                Version 5 Successfully Deployed!
            </div>

            <p class="success">
                ✓ Application deployed automatically using GitOps
            </p>

            <div class="pipeline">
                💻 Code
                →
                🧪 Test
                →
                🐳 Build
                →
                📦 Release
                →
                🚀 Deploy
                →
                ☸️ Kubernetes
            </div>

            <h3>GitHub Actions + Docker Hub + Argo CD</h3>

            <p>
                This application was tested, containerized, released,
                and deployed through an automated CI/CD pipeline.
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)