pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Windows\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Windows\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t aceest-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 aceest-app'
            }
        }
    }
}