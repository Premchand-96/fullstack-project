pipeline {
    agent any

    environment {
        EC2_USER = "ubuntu"
        EC2_HOST = "3.90.35.201"
        KEY_PATH = "/var/lib/jenkins/keys/ec2-key.pem"

        BACKEND_PATH = "/home/ubuntu/fullstack-project/backend"
        FRONTEND_PATH = "/home/ubuntu/fullstack-project/frontend"
        NGINX_PATH = "/var/www/fullstack"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Premchand-96/fullstack-project.git'
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

        stage('Deploy Backend + Frontend to EC2') {
            steps {
                sh '''
                chmod 600 $KEY_PATH

                # Create folders if not exist
                ssh -i $KEY_PATH -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST "
                    mkdir -p /home/ubuntu/fullstack-project/backend
                    sudo mkdir -p /var/www/fullstack
                "

                # Copy backend
                rsync -avz -e "ssh -i $KEY_PATH -o StrictHostKeyChecking=no" backend/ \
                $EC2_USER@$EC2_HOST:$BACKEND_PATH

                # Copy frontend build (IMPORTANT: dist folder)
                rsync -avz -e "ssh -i $KEY_PATH -o StrictHostKeyChecking=no" frontend/dist/ \
                $EC2_USER@$EC2_HOST:$NGINX_PATH
                '''
            }
        }

        stage('Restart Services on EC2') {
            steps {
                sh '''
                ssh -i $KEY_PATH -o StrictHostKeyChecking=no $EC2_USER@$EC2_HOST << 'EOF'

                echo "Restarting backend..."

                sudo systemctl daemon-reload
                sudo systemctl restart fastapi
                sudo systemctl enable fastapi

                echo "Restarting nginx..."
                sudo systemctl restart nginx

                echo "Deployment complete 🚀"

EOF
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment SUCCESS"
        }
        failure {
            echo "❌ Deployment FAILED"
        }
    }
}
