pipeline {
    agent any

    environment {
        APP_NAME     = 'student-app'
        IMAGE_TAG    = 'student-app:latest'
        CONTAINER_PORT = 5000
        HOST_PORT    = 5000
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo '=== Stage 1: Checkout Source Code ==='
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '=== Stage 2: Installing Dependencies ==='
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo '=== Stage 3: Running Automated Pytest Suite ==='
                bat 'pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '=== Stage 4: Building Container Image ==='
                bat 'docker build -t %IMAGE_TAG% .'
            }
        }

        stage('Deploy Container') {
            steps {
                echo '=== Stage 5: Deploying Docker Container ==='
                bat '''
                    docker stop %APP_NAME% 2>nul || exit 0
                    docker rm %APP_NAME% 2>nul || exit 0
                    docker run -d -p %HOST_PORT%:%CONTAINER_PORT% --name %APP_NAME% %IMAGE_TAG%
                '''
            }
        }

        stage('Health & Monitoring Verification') {
            steps {
                echo '=== Stage 6: Verifying Health Check & Monitoring ==='
                bat '''
                    powershell -Command "Start-Sleep -Seconds 5; try { $res = Invoke-RestMethod -Uri http://localhost:5000/health; Write-Host 'Health status:' $res.status } catch { Write-Error 'Health check failed' }"
                    docker ps --filter "name=%APP_NAME%"
                '''
            }
        }
    }

    post {
        success {
            echo '=== Pipeline Execution Succeeded! Application deployed & healthy. ==='
        }
        failure {
            echo '=== Pipeline Execution Failed! Check console log for details. ==='
        }
    }
}
