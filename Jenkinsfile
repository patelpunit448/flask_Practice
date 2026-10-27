pipeline {
    agent any

    options {
        disableConcurrentBuilds()
        timeout(time: 15, unit: 'MINUTES')
    }

    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Prepare Python Environment') {
            steps {
                echo 'Creating Python environment without sudo or Docker...'

                sh '''
                    set -eu

                    python3 --version

                    # Remove only the previous workspace virtual environment.
                    rm -rf -- .venv
                    mkdir -p .jenkins-tools

                    # Download virtualenv using Python; curl/wget are not required.
                    python3 - <<'PY'
import pathlib
import sys
import urllib.request

version = f"{sys.version_info.major}.{sys.version_info.minor}"
url = f"https://bootstrap.pypa.io/virtualenv/{version}/virtualenv.pyz"
target = pathlib.Path(".jenkins-tools/virtualenv.pyz")

print(f"Downloading virtualenv for Python {version}")
with urllib.request.urlopen(url, timeout=60) as response:
    target.write_bytes(response.read())
PY

                    python3 .jenkins-tools/virtualenv.pyz .venv

                    .venv/bin/python --version
                    .venv/bin/python -m pip --version
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Installing application dependencies...'

                sh '''
                    set -eu

                    if [ ! -f requirements.txt ]; then
                        echo "ERROR: requirements.txt is missing from the repository root."
                        exit 1
                    fi

                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Checking installed dependency compatibility...'

                sh '''
                    set -eu
                    .venv/bin/python -m pip check
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment not configured: no deployment target supplied.'
                echo 'Add your actual deployment commands here.'
            }
        }
    }

    post {
        success {
            echo 'Environment setup, dependency installation, and dependency checks passed.'
            echo 'No application deployment was performed.'
        }

        failure {
            echo 'Pipeline failed. Check the first error in the console output.'
        }
    }
}