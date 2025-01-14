pipeline {
    agent none
    
    environment {
        GITHUB_CREDENTIALS = credentials('github-credentials')
        ARTIFACT_DIR = 'build-artifacts'
    }
    
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }
    
    stages {
        stage('Parallel Platform Builds') {
            parallel {
                stage('Linux Build') {
                    agent {
                        label 'linux'
                    }
                    stages {
                        stage('Checkout') {
                            steps {
                                checkout scm
                            }
                        }
                        stage('Setup') {
                            steps {
                                sh '''
                                    python3 -m venv venv
                                    . venv/bin/activate
                                    pip install -r requirements.txt
                                '''
                            }
                        }
                        stage('Test') {
                            steps {
                                sh '''
                                    . venv/bin/activate
                                    pytest tests/ --junitxml=test-results/linux-results.xml
                                '''
                            }
                        }
                        stage('Build') {
                            steps {
                                sh '''
                                    . venv/bin/activate
                                    python setup.py bdist_wheel
                                '''
                            }
                        }
                        stage('Archive') {
                            steps {
                                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                                junit 'test-results/*.xml'
                            }
                        }
                    }
                }
                
                stage('Windows Build') {
                    agent {
                        label 'windows'
                    }
                    stages {
                        stage('Checkout') {
                            steps {
                                checkout scm
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
                                    pytest tests/ --junitxml=test-results/windows-results.xml
                                '''
                            }
                        }
                        stage('Build') {
                            steps {
                                bat '''
                                    call venv\\Scripts\\activate.bat
                                    python setup.py bdist_wheel
                                '''
                            }
                        }
                        stage('Archive') {
                            steps {
                                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                                junit 'test-results/*.xml'
                            }
                        }
                    }
                }
                
                stage('MacOS Build') {
                    agent {
                        label 'macos'
                    }
                    stages {
                        stage('Checkout') {
                            steps {
                                checkout scm
                            }
                        }
                        stage('Setup') {
                            steps {
                                sh '''
                                    python3 -m venv venv
                                    . venv/bin/activate
                                    pip install -r requirements.txt
                                '''
                            }
                        }
                        stage('Test') {
                            steps {
                                sh '''
                                    . venv/bin/activate
                                    pytest tests/ --junitxml=test-results/macos-results.xml
                                '''
                            }
                        }
                        stage('Build') {
                            steps {
                                sh '''
                                    . venv/bin/activate
                                    python setup.py bdist_wheel
                                '''
                            }
                        }
                        stage('Archive') {
                            steps {
                                archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
                                junit 'test-results/*.xml'
                            }
                        }
                    }
                }
            }
        }
    }
    
    post {
        always {
            node('master') {
                emailext subject: "Build ${currentBuild.currentResult}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                         body: """Build status: ${currentBuild.currentResult}
                                 Build URL: ${env.BUILD_URL}
                                 Build Number: ${env.BUILD_NUMBER}""",
                         recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            }
        }
    }
}