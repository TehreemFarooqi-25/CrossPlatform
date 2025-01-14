pipeline {
    agent any
    
    options {
        // Clean workspace before build
        cleanWs()
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    environment {
        GITHUB_REPO = 'https://github.com/TehreemFarooqi-25/CrossPlatform.git'
        BRANCH_NAME = 'main'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Clean workspace
                deleteDir()
                // Explicit git checkout
                git branch: env.BRANCH_NAME,
                    url: env.GITHUB_REPO
            }
        }
        
        stage('Setup') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    mkdir test-results
                    pytest tests/ --junitxml=test-results/results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-results/*.xml'
                }
            }
        }
        
        stage('Build') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    python setup.py bdist_wheel
                '''
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
            echo "Pipeline finished - cleaning workspace"
        }
        success {
            echo "Build completed successfully"
        }
        failure {
            echo "Build failed"
        }
    }
}