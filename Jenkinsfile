pipeline {
    agent { dockerfile true }
    stages {
        stage("Install dependencies") {
            steps {
                sh 'pip install --user --upgrade pip'
                sh 'pip install --user -r requirements.txt'
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