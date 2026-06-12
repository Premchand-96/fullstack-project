pipeline {
agent any

```
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

    stage('Deploy Frontend to Nginx') {
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
            '''
        }
    }

    stage('Verify Services') {
        steps {
            sh '''
            sudo systemctl is-active nginx
            sudo systemctl is-active fastapi
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
