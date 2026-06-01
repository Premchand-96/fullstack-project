pipeline {
    agent any

    environment {
        EC2_HOST = "34.206.52.251"
        EC2_USER = "ubuntu"
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
                python3 -m venv venv
                ./venv/bin/pip install -r requirements.txt
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

        stage('Deploy to EC2 (NO SSH AGENT)') {
            steps {
                sh '''
                echo "Deploying using direct SSH key..."

                ssh -o StrictHostKeyChecking=no ubuntu@34.206.52.251 << 'EOF'

                mkdir -p /home/ubuntu/fullstack-project/fullstack-project

                EOF

                rsync -avz -e "ssh -o StrictHostKeyChecking=no" backend/ \
                ubuntu@34.206.52.251:/home/ubuntu/fullstack-project/fullstack-project/backend

                rsync -avz -e "ssh -o StrictHostKeyChecking=no" frontend/dist/ \
                ubuntu@34.206.52.251:/home/ubuntu/fullstack-project/fullstack-project/frontend/dist
                '''
            }
        }

        stage('Restart Services') {
            steps {
                sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@34.206.52.251 << 'EOF'

                sudo systemctl daemon-reload
                sudo systemctl restart fastapi || true
                sudo systemctl restart nginx

                EOF
                '''
            }
        }
    }

    post {
        success {
            echo "🚀 Deployment Successful"
        }
        failure {
            echo "❌ Deployment Failed"
        }
    }
}
