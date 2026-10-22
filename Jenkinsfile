pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Dippss99/stqa-continuous-testing..git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }

    post {
        success {
            echo 'All tests passed! Build: SUCCESS'
        }
        failure {
            echo 'Some tests failed. Build: FAILURE'
        }
    }
}
