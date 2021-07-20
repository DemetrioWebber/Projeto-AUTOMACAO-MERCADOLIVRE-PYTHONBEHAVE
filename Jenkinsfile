pipeline {
    agent {
        docker { dockerfile true }
    }
    stages {
        stage("Install dependencies") {
            steps {
                sh 'pip install -r requirements.txt'
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