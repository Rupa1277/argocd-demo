from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Argo CD CI/CD Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 800px;
                margin: auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            h1 {
                margin-bottom: 5px;
            }

            .subtitle {
                color: #666;
                margin-bottom: 30px;
            }

            .status {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
            }

            .card {
                padding: 20px;
                border-radius: 8px;
                background: #f8f9fa;
                border-left: 5px solid #28a745;
            }

            .label {
                font-size: 14px;
                color: #666;
            }

            .value {
                font-size: 20px;
                font-weight: bold;
                margin-top: 5px;
            }

            .pipeline {
                margin-top: 30px;
                padding: 20px;
                background: #eef3ff;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
            }

            .footer {
                margin-top: 30px;
                text-align: center;
                color: #666;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>🚀 Argo CD CI/CD Demonstration</h1>

            <div class="subtitle">
                GitOps-based Continuous Delivery on Kubernetes
            </div>

            <div class="status">

                <div class="card">
                    <div class="label">Application</div>
                    <div class="value">Flask Demo</div>
                </div>

                <div class="card">
                    <div class="label">Version</div>
                    <div class="value">1.0</div>
                </div>

                <div class="card">
                    <div class="label">CI Status</div>
                    <div class="value">✓ PASSED</div>
                </div>

                <div class="card">
                    <div class="label">CD Status</div>
                    <div class="value">✓ SYNCED</div>
                </div>

                <div class="card">
                    <div class="label">Platform</div>
                    <div class="value">Kubernetes</div>
                </div>

                <div class="card">
                    <div class="label">Deployment Tool</div>
                    <div class="value">Argo CD</div>
                </div>

            </div>

            <div class="pipeline">

                GitHub Actions
                →
                Docker Hub
                →
                Argo CD
                →
                Kubernetes

            </div>

            <div class="footer">

                GitOps Status:
                <strong>DESIRED STATE = ACTUAL STATE</strong>

                <br><br>

                Continuous Delivery Demonstration

            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)