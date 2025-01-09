pipeline {
    // Run on any available agent
    agent any
    
    // Define environment variables
    environment {
        GITHUB_REPO = 'https://github.com/TehreemFarooqi-25/CrossPlatform.git'
        BRANCH_NAME = 'main'
    }
    
    // Configure different platforms
    matrix {
        axes {
            axis {
                name 'PLATFORM'
                values 'linux', 'windows', 'macos'
            }
        }
        
        stages {
            // Checkout code from version control
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }
            
            // Install dependencies based on platform
            stage('Setup Environment') {
                steps {
                    script {
                        switch(PLATFORM) {
                            case 'linux':
                                sh 'python3 -m pip install -r requirements.txt'
                                break
                            case 'windows':
                                bat 'python -m pip install -r requirements.txt'
                                break
                            case 'macos':
                                sh 'python3 -m pip install -r requirements.txt'
                                break
                        }
                    }
                }
            }
            
            // Run tests
            stage('Run Tests') {
                steps {
                    script {
                        switch(PLATFORM) {
                            case 'linux':
                                sh 'python3 -m pytest tests/'
                                break
                            case 'windows':
                                bat 'python -m pytest tests/'
                                break
                            case 'macos':
                                sh 'python3 -m pytest tests/'
                                break
                        }
                    }
                }
            }
            
            // Execute the code
            stage('Run Code') {
                steps {
                    script {
                        switch(PLATFORM) {
                            case 'linux':
                                sh 'python3 main.py'
                                break
                            case 'windows':
                                bat 'python main.py'
                                break
                            case 'macos':
                                sh 'python3 main.py'
                                break
                        }
                    }
                }
            }
        }
    }
    
    // Post-build actions
    post {
        success {
            echo "Pipeline completed successfully on ${PLATFORM}"
        }
        failure {
            echo "Pipeline failed on ${PLATFORM}"
            // Add notification steps here (email, Slack, etc.)
        }
        always {
            cleanWs()
        }
    }
}