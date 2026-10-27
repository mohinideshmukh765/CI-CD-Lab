# CI/CD Pipeline & Monitoring Lab

**Student Name:** Mohini Deshmukh  
**PRN / Roll Number:** 2425010071 (Roll No: DS-76)  
**Department / Class:** Department of CSE (Data Science) / Final Year B.Tech CSE (DS), Semester VII  
**Academic Year:** A.Y. 2026-27  
**Course:** DevOps & Cloud Computing / ISE-2 Lab  

---

## 1. Project Overview

This project implements a complete DevOps Continuous Integration and Continuous Deployment (CI/CD) lifecycle for a Python Flask microservice on a Windows PC. It integrates:

- **Version Control:** Git
- **Source Code Hosting:** GitHub
- **Application Containerization:** Docker
- **Continuous Integration & Automation:** Jenkins
- **Monitoring & Observability:** Endpoint Health Checks (`/health`), System Metrics (`/metrics`), and Docker Container Inspection

---

## 2. Project Architecture & Directory Structure

```
C:\CI-CD-Lab\
├── app.py                     # Flask web application with health & metrics endpoints
├── requirements.txt           # Python application dependencies
├── Dockerfile                 # Container image definition with healthcheck
├── .dockerignore              # Files excluded from Docker build context
├── .gitignore                 # Files excluded from Git version control
├── Jenkinsfile                # Declarative Jenkins CI/CD pipeline definition
├── README.md                  # Project documentation and operational guide
└── tests/
    └── test_app.py            # Automated unit and integration test suite
```

---

## 3. Endpoints & API Specification

| Endpoint | Method | Purpose | Response Format |
|---|---|---|---|
| `/` | GET | Interactive Web Dashboard showing student metadata & service status | HTML |
| `/health` | GET | Service liveness and component health check | JSON (`{"status": "UP", ...}`) |
| `/metrics` | GET | Application telemetry (requests, uptime, OS specs) | JSON |
| `/info` | GET | Application metadata and developer information | JSON |

---

## 4. Local Execution & Testing Guide

### 4.1 Prerequisites
- Python 3.11+
- Git for Windows
- Docker Desktop
- Jenkins & Java 21 LTS

### 4.2 Setup Virtual Environment
```powershell
cd C:\CI-CD-Lab
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 4.3 Run Automated Tests
```powershell
pytest tests/ -v
```

### 4.4 Run the Application Locally
```powershell
python app.py
```
Visit: `http://localhost:5000`

---

## 5. Docker Containerization

### 5.1 Build the Image
```powershell
docker build -t student-app .
```

### 5.2 Run the Container
```powershell
docker run -d -p 5000:5000 --name student-app student-app
```

### 5.3 Verify Container Execution & Health
```powershell
docker ps
docker logs student-app
docker inspect --format='{{json .State.Health}}' student-app
```

---

## 6. Jenkins Pipeline Execution

The pipeline automates:
1. **Checkout SCM:** Pulls latest code from Git.
2. **Install Dependencies:** Installs required packages into the environment.
3. **Run Automated Tests:** Executes `pytest` to gate defects before containerization.
4. **Build Docker Image:** Packages the application into `student-app:latest`.
5. **Deploy Container:** Restarts container with port mapping `5000:5000`.
6. **Health & Monitoring Verification:** Validates `http://localhost:5000/health`.
