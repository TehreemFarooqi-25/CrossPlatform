pipeline {
    // Run on any available agent
    agent any
    
    // Define environment variables
    environment {
        GITHUB_REPO = 'https://github.com/TehreemFarooqi-25/CrossPlatform.git'
        BRANCH_NAME = 'main'
    }
    
    // Define stages
    stages {
        // Checkout code from version control
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        // Setup environment and run code for different platforms in parallel
        stage('Run on Different Platforms') {
            parallel {
                // Linux platform
                linux: {
                    steps {
                        script {
                            sh 'python3 -m pip install -r requirements.txt'
                            sh 'python3 -m pytest tests/'
                            sh 'python3 main.py'
                        }
                    }
                }
                
                // Windows platform
                windows: {
                    steps {
                        script {
                            bat 'python -m pip install -r requirements.txt'
                            bat 'python -m pytest tests/'
                            bat 'python main.py'
                        }
                    }
                }

                // macOS platform
                macos: {
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

    // Post-build actions
    post {
        success {
            echo "Pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed."
            // Add notification steps here (email, Slack, etc.)
        }
        always {
            cleanWs()
        }
    }
}
