from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

FEATURES = [
    {
        "name": "Homepage",
        "description": "The main dashboard of the Feature Tracker application.",
        "status": "Active"
    },
    {
        "name": "About Page",
        "description": "Information about the application and its DevOps automation.",
        "status": "Active"
    }
]


@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Feature Tracker</title>

        <style>
            * {
                box-sizing: border-box;
            }
            /*
            */

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                color: #333;
            }

            .navbar {
                background: #1f2937;
                color: white;
                padding: 18px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .logo {
                font-size: 24px;
                font-weight: bold;
            }

            .badge {
                background: #22c55e;
                padding: 7px 14px;
                border-radius: 20px;
                font-size: 14px;
            }

            .container {
                width: 84%;
                margin: 40px auto;
            }

            .hero {
                background: white;
                padding: 35px;
                border-radius: 14px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
                margin-bottom: 30px;
            }

            h1 {
                margin-top: 0;
                color: #111827;
            }

            .subtitle {
                color: #6b7280;
                font-size: 17px;
            }

            .stats {
                display: flex;
                gap: 20px;
                margin-bottom: 30px;
            }

            .stat-card {
                background: white;
                flex: 1;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            }

            .stat-number {
                font-size: 32px;
                font-weight: bold;
                color: #2563eb;
            }

            .stat-label {
                color: #6b7280;
                margin-top: 5px;
            }

            .section-title {
                margin-bottom: 20px;
            }

            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }

            .feature-card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            }

            .feature-card h3 {
                margin-top: 0;
            }

            .status {
                display: inline-block;
                margin-top: 12px;
                background: #dcfce7;
                color: #166534;
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 13px;
                font-weight: bold;
            }

            footer {
                text-align: center;
                color: #6b7280;
                padding: 30px;
            }

            @media (max-width: 700px) {
                .stats {
                    flex-direction: column;
                }

                .container {
                    width: 92%;
                }
            }
        </style>
    </head>

    <body>

        <div class="navbar">
            <div class="logo">Feature Tracker</div>
            <div class="badge">System Healthy</div>
        </div>

        <div class="container">

            <div class="hero">
                <h1>Welcome to Feature Tracker</h1>

                <p class="subtitle">
                    A simple application used to demonstrate automated CI/CD
                    and GitOps deployment using GitHub Actions, Docker,
                    Kubernetes, and Argo CD.
                </p>
            </div>

            <div class="stats">

                <div class="stat-card">
                    <div class="stat-number">{{ features|length }}</div>
                    <div class="stat-label">Active Features</div>
                </div>

                <div class="stat-card">
                    <div class="stat-number">2</div>
                    <div class="stat-label">Running Replicas</div>
                </div>

                <div class="stat-card">
                    <div class="stat-number">Healthy</div>
                    <div class="stat-label">Application Status</div>
                </div>

            </div>

            <h2 class="section-title">Application Features</h2>

            <div class="feature-grid">

                {% for feature in features %}
                <div class="feature-card">

                    <h3>{{ feature.name }}</h3>

                    <p>{{ feature.description }}</p>

                    <span class="status">
                        {{ feature.status }}
                    </span>

                </div>
                {% endfor %}

            </div>

        </div>

        <footer>
            Feature Tracker • GitOps Demonstration using Argo CD
        </footer>

    </body>
    </html>
    """, features=FEATURES)


@app.route("/about")
def about():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About - Feature Tracker</title>

        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                color: #333;
            }

            .navbar {
                background: #1f2937;
                color: white;
                padding: 18px 8%;
            }

            .container {
                width: 75%;
                margin: 50px auto;
                background: white;
                padding: 40px;
                border-radius: 14px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }

            h1 {
                color: #2563eb;
            }

            .back {
                display: inline-block;
                margin-top: 25px;
                padding: 10px 18px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }
        </style>
    </head>

    <body>

        <div class="navbar">
            <strong>Feature Tracker</strong>
        </div>

        <div class="container">

            <h1>About This Application</h1>

            <p>
                Feature Tracker is a demonstration application designed to
                showcase a complete DevOps and GitOps workflow.
            </p>

            <p>
                Application changes are tested and built automatically using
                GitHub Actions. Docker images are released to Docker Hub, and
                Argo CD continuously monitors the Git repository and deploys
                changes to Kubernetes automatically.
            </p>

            <p>
                The application also demonstrates Argo CD features such as
                automated synchronization, self-healing, health monitoring,
                and rollback.
            </p>

            <a href="/" class="back">← Back to Dashboard</a>

        </div>

    </body>
    </html>
    """)


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        application="Feature Tracker",
        features=len(FEATURES)
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)