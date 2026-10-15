pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'YOUR_GITHUB_REPOSITORY_URL'
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
