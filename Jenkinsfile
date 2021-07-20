pipeline {
    agent { dockerfile true }
    stages {
        stage("Run tests") {
            steps {
                dir('bdd'){
                    sh 'behave --tags "@scenario.notebook_dell"'
                }
            }
        }
    }
}