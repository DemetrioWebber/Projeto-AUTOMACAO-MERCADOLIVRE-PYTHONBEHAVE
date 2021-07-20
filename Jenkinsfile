pipeline {
    agent { dockerfile true }
    stages {
        stage("Install dependencies") {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage("Run tests") {
            steps {
                dir('bdd'){
                    sh 'behave --tags "@scenario.notebook_dell"'
                }
            }
        }
    }
}