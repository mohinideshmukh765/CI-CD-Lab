import os
import platform
import time
from datetime import datetime
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)
START_TIME = time.time()
REQUEST_COUNT = 0

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps CI/CD Lab Application</title>
    <style>
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --accent: #38bdf8;
            --accent-green: #4ade80;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        body {
            background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 1rem;
        }
        .container {
            max-width: 820px;
            width: 100%;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            backdrop-filter: blur(12px);
            padding: 2.5rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }
        .badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(74, 222, 128, 0.15);
            color: var(--accent-green);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 1.25rem;
            border: 1px solid rgba(74, 222, 128, 0.3);
        }
        .badge-dot {
            width: 8px;
            height: 8px;
            background: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--accent-green);
        }
        h1 {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p.subtitle {
            color: var(--text-muted);
            margin-bottom: 2rem;
            font-size: 1.05rem;
        }
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.25rem;
            margin-bottom: 2rem;
        }
        .info-card {
            background: rgba(0, 0, 0, 0.25);
            padding: 1.25rem;
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .info-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 0.35rem;
        }
        .info-value {
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
        }
        .links-container {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            margin-top: 1.5rem;
        }
        a.btn {
            background: rgba(56, 189, 248, 0.15);
            color: var(--accent);
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            border: 1px solid rgba(56, 189, 248, 0.3);
            transition: all 0.2s ease;
        }
        a.btn:hover {
            background: var(--accent);
            color: #0f172a;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
        }
        footer {
            margin-top: 2rem;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="badge">
            <div class="badge-dot"></div>
            Application Status: Healthy & Running
        </div>
        <h1>CI/CD Pipeline & Monitoring Lab</h1>
        <p class="subtitle">Demonstration of automated deployment, containerization, and monitoring lifecycle.</p>

        <div class="info-grid">
            <div class="info-card">
                <div class="info-label">Student Name</div>
                <div class="info-value">{{ student_name }}</div>
            </div>
            <div class="info-card">
                <div class="info-label">PRN / Roll Number</div>
                <div class="info-value">{{ roll_no }}</div>
            </div>
            <div class="info-card">
                <div class="info-label">Department / Class</div>
                <div class="info-value">{{ department }}</div>
            </div>
            <div class="info-card">
                <div class="info-label">Academic Year</div>
                <div class="info-value">{{ academic_year }}</div>
            </div>
            <div class="info-card">
                <div class="info-label">App Version</div>
                <div class="info-value">{{ version }}</div>
            </div>
            <div class="info-card">
                <div class="info-label">Host Platform</div>
                <div class="info-value">{{ platform_name }}</div>
            </div>
        </div>

        <div class="links-container">
            <a href="/health" class="btn">/health (Health-Check)</a>
            <a href="/metrics" class="btn">/metrics (System Metrics)</a>
            <a href="/info" class="btn">/info (API Metadata)</a>
        </div>
    </div>
    <footer>
        DevOps Continuous Integration & Continuous Delivery Pipeline &bull; ISE-2 Lab
    </footer>
</body>
</html>
"""

@app.before_request
def count_requests():
    global REQUEST_COUNT
    REQUEST_COUNT += 1

@app.route("/")
def index():
    return render_template_string(
        HTML_TEMPLATE,
        student_name="Shivam Korpade",
        roll_no="2324000756 (DS38)",
        department="B.Tech CSE (Data Science) - Sem VII",
        academic_year="A.Y. 2026-27",
        version="1.0.0",
        platform_name="LAPTOP-UNKNOWN"
    )

@app.route("/health")
def health():
    uptime = time.time() - START_TIME
    return jsonify({
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "uptime_seconds": round(uptime, 2),
        "version": "1.0.0",
        "checks": {
            "application": "UP",
            "memory": "UP",
            "storage": "UP"
        }
    }), 200

@app.route("/metrics")
def metrics():
    uptime = time.time() - START_TIME
    return jsonify({
        "total_requests": REQUEST_COUNT,
        "uptime_seconds": round(uptime, 2),
        "python_version": platform.python_version(),
        "system_os": platform.system(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }), 200

@app.route("/info")
def info():
    return jsonify({
        "app_name": "CI-CD-Lab-App",
        "description": "Flask microservice demonstrating CI/CD pipeline automation and endpoint monitoring",
        "author": "Shivam Korpade",
        "prn": "2324000756",
        "academic_year": "2026-27",
        "version": "1.0.0"
    }), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found", "code": 404}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error", "code": 500}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
