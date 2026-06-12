pipeline {
    agent any

    environment {
        APP_DIR = "/home/ubuntu/fullstack-project"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Premchand-96/fullstack-project.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh '''
                cd backend

                rm -rf venv

                python3 -m venv venv

                venv/bin/python -m pip install --upgrade pip

                if [ -f requirements.txt ]; then
                    venv/bin/python -m pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Build Frontend') {
            steps {
                sh '''
                cd frontend

                npm install
                npm run build
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                sudo rsync -av --delete backend/ ${APP_DIR}/backend/
                sudo rsync -av --delete frontend/dist/ /var/www/html/
                '''
            }
        }

        stage('Restart Services') {
            steps {
                sh '''
                sudo systemctl restart fastapi
                sudo systemctl restart nginx

                sudo systemctl status fastapi --no-pager
                sudo systemctl status nginx --no-pager
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful'
        }

        failure {
            echo '❌ Deployment Failed'
        }
    }
}
