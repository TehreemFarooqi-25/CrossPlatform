pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/TehreemFarooqi-25/CrossPlatform.git'
        BRANCH_NAME = 'main'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Explicit git checkout instead of checkout scm
                git branch: env.BRANCH_NAME,
                    url: env.GITHUB_REPO
            }
        }
        
        stage('Run on Different Platforms') {
            parallel {
                stage('Linux') {
                    steps {
                        script {
                            sh 'python3 -m pip install -r requirements.txt'
                            sh 'python3 -m pytest tests/'
                            sh 'python3 main.py'
                        }
                    }
                }
                
                stage('Windows') {
                    steps {
                        script {
                            bat 'python -m pip install -r requirements.txt'
                            bat 'python -m pytest tests/'
                            bat 'python main.py'
                        }
                    }
                }
                
                stage('MacOS') {
                    steps {
                        script {
                            sh 'python3 -m pip install -r requirements.txt'
                            sh 'python3 -m pytest tests/'
                            sh 'python3 main.py'
                        }
                    }
                }
            }
        }
    }
    
    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed."
        }
        always {
            cleanWs()
        }
    }
}