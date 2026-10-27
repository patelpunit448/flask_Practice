pipeline {
    agent any

    environment {
        // Optional: define any environment variables you need
        VENV = 'venv'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests with pytest...'
                sh '''
                    . ${VENV}/bin/activate
                    pytest --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    // Publish test results so they appear in the Jenkins UI
                    junit 'test-results.xml'
                }
            }
        }

        stage('Deploy') {
            when {
                // Only run if previous stages succeeded
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                echo 'Deploying to Staging environment...'
                sh '''
                    . ${VENV}/bin/activate

                    # --- Replace the section below with your actual deployment method ---

                    # Example 1: Simple copy / rsync to a staging server
                    # rsync -avz --delete ./ user@staging-server:/opt/myapp/

                    # Example 2: Docker-based deployment
                    # docker build -t myapp:staging .
                    # docker push myregistry/myapp:staging
                    # ssh user@staging-server "docker pull myregistry/myapp:staging && docker-compose up -d"

                    # Example 3: Call a deployment script
                    # ./deploy.sh staging

                    echo "Deployment to Staging completed successfully"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            // Clean up the virtual environment (optional)
            sh 'rm -rf ${VENV}'
        }
    }
}