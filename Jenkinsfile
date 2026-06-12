pipeline {
agent any

```
environment {
    APP_DIR = "/home/ubuntu/fullstack-project"
    NGINX_DIR = "/var/www/html"
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

            ./venv/bin/python -m pip install --upgrade pip
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

    stage('Deploy Frontend') {
        steps {
            sh '''
            sudo rm -rf /var/www/html/*
            sudo cp -r frontend/dist/* /var/www/html/
            '''
        }
    }

    stage('Restart Services') {
        steps {
            sh '''
            sudo systemctl restart nginx
            sudo systemctl restart fastapi

            sudo systemctl status nginx --no-pager
            sudo systemctl status fastapi --no-pager
            '''
        }
    }
}

post {
    success {
        echo 'Deployment Successful'
    }

    failure {
        echo 'Deployment Failed'
    }
}
```

}
