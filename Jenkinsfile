pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/TehreemFarooqi-25/CrossPlatform.git'
        BRANCH_NAME = 'main'
    }
    
    stages {
        // Checkout code from version control
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Run on different platforms in parallel
        stage('Run on Different Platforms') {
            parallel {
                linux: {
                    stage('Linux Setup') {
                        steps {
                            script {
                                sh 'python3 -m pip install -r requirements.txt'
                                sh 'python3 -m pytest tests/'
                                sh 'python3 main.py'
                            }
                        }
                    }
                },
                
                windows: {
                    stage('Windows Setup') {
                        steps {
                            script {
                                bat 'python -m pip install -r requirements.txt'
                                bat 'python -m pytest tests/'
                                bat 'python main.py'
                            }
                        }
                    }
                },
                
                macos: {
                    stage('MacOS Setup') {
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
