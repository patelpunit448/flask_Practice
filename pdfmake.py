Here is the updated documentation and generator. 

The previous placeholder screenshot links have been removed and replaced with your actual UI screenshots tracking the full application lifecycle: **Home View (Initial)**, **Add Student View**, **Home View (Record Added)**, **Update Student View**, and **Home View (Record Updated)**.

---

### Step 1: Save Your Local Screenshots
Save the 5 images you provided into a folder named `screenshots/` inside your project root directory with these exact file names:

* `screenshots/01_home_initial.png` *(Initial student list)*
* `screenshots/02_add_student.png` *(Add Student form with "Punit")*
* `screenshots/03_home_added.png` *(List showing "Punit" added)*
* `screenshots/04_update_student.png` *(Update Student form)*
* `screenshots/05_home_updated.png` *(List showing updated name "Punit Patel")*

---

### Step 2: Updated `README.md`

```markdown
# Student Registration System

A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap 5

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **CI/CD:** Jenkins, GitHub Actions
* **Testing:** Pytest

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/mohanDevOps-arch/flask_Practice.git
cd flask_Practice
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```env
MONGO_URI=<your-mongodb-connection-string>
SECRET_KEY=<your-secret-key>
```

### 5. Run the application
```bash
python app.py
```
Open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Application Walkthrough & Screenshots

### 1. Home Page (Initial State)
Displays existing registered students with options to Edit or Delete records.
![Home Initial](screenshots/01_home_initial.png)

### 2. Add Student
Form to register a new student with details: Name, Email, and Course.
![Add Student](screenshots/02_add_student.png)

### 3. Home Page (New Record Added)
Student list dynamically updated with the newly added record (`Punit`).
![Home Added](screenshots/03_home_added.png)

### 4. Update Student
Form pre-populated with student details ready for editing.
![Update Student](screenshots/04_update_student.png)

### 5. Home Page (Updated Record)
Reflects the saved modifications (`Punit Patel`).
![Home Updated](screenshots/05_home_updated.png)

---

## CI/CD Pipeline Automation

### 1. Jenkins Pipeline
* **Trigger:** GitHub webhook pushes to `main`.
* **Stages:**
  1. *Build*: Virtual environment initialization and dependency installation via `pip`.
  2. *Test*: Automated test execution via `pytest`.
  3. *Deploy to Staging*: Code transfer and service restart on the staging host.
* **Alerts:** Automated email notification on pipeline success or failure via `emailext`.

### 2. GitHub Actions Workflow
* **Trigger:** Pushes/PRs to `main` and `staging`, and release tags (`v*.*.*`).
* **Jobs:**
  * `test`: Runs dependencies check and Pytest unit tests.
  * `deploy-staging`: Automatic deployment to Staging environment on push to `staging`.
  * `deploy-production`: Automated deployment to Production environment triggered upon release tag creation.

---

## License
MIT License
```

---

### Step 3: Run the Script to Build the Merged PDF

Run this standalone script to produce a single, unified PDF document (**`flask_app_cicd_complete.pdf`**) containing:
1. Jenkins CI/CD documentation and complete `Jenkinsfile`.
2. GitHub Actions workflow specification and secrets table.
3. The embedded walkthrough screenshots showing the exact flow.

```python
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Preformatted, Image, KeepTogether
)

def build_pdf(filename="flask_app_cicd_complete.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36, leftMargin=36,
        topMargin=36, bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=6
    )
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['BodyText'],
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#4A5568")
    )
    code_style = ParagraphStyle(
        'CodeStyle',
        fontName="Courier",
        fontSize=7,
        leading=9.5,
        textColor=colors.HexColor("#1A202C")
    )

    story = []

    # Title & Introduction
    story.append(Paragraph("Student Registration System - CI/CD & Application Manual", title_style))
    story.append(Paragraph("Automated DevOps Architecture: Jenkins, GitHub Actions & Test Validation", body_style))
    story.append(Spacer(1, 10))

    # SECTION 1: Jenkins
    story.append(Paragraph("1. Jenkins CI/CD Pipeline Implementation", h1_style))
    story.append(Paragraph(
        "Automated deployment pipeline running on Jenkins. Triggered on code pushes to the main branch via "
        "GitHub webhooks. Executes clean virtualenv builds, pytest runs, deployment over SSH, and email notifications.",
        body_style
    ))
    story.append(Spacer(1, 4))

    jenkins_code = """pipeline {
    agent any
    environment {
        PYTHON_VENV  = "venv"
        MONGO_URI    = credentials('MONGO_URI_SECRET')
        STAGING_HOST = "ubuntu@staging.example.com"
    }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Build & Dependencies') {
            steps {
                sh '''
                    python3 -m venv ${PYTHON_VENV}
                    . ${PYTHON_VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh '. ${PYTHON_VENV}/bin/activate && pytest --disable-warnings -v'
            }
        }
        stage('Deploy to Staging') {
            when { branch 'main' }
            steps {
                sshagent(['staging-ssh-key']) {
                    sh 'echo "Deploying application to Staging VM..."'
                    // rsync -avz --exclude "venv" . ${STAGING_HOST}:/var/www/flask_app
                    // ssh ${STAGING_HOST} "sudo systemctl restart flaskapp"
                }
            }
        }
    }
    post {
        success { emailext (subject: "SUCCESS: Build #${env.BUILD_NUMBER}", body: "Build passed tests and deployed successfully.", to: "devops@example.com") }
        failure { emailext (subject: "FAILED: Build #${env.BUILD_NUMBER}", body: "Build or test failed.", to: "devops@example.com") }
    }
}"""
    t_jenkins = Table([[Preformatted(jenkins_code, code_style)]], colWidths=[540])
    t_jenkins.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EDF2F7")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_jenkins)
    story.append(Spacer(1, 10))

    # SECTION 2: GitHub Actions
    story.append(Paragraph("2. GitHub Actions CI/CD Pipeline Workflow", h1_style))
    story.append(Paragraph(
        "Configured in .github/workflows/ci-cd.yml. Validates code on push/pull request. "
        "Deploys to Staging from the 'staging' branch, and to Production when a Git tag is released.",
        body_style
    ))
    story.append(Spacer(1, 4))

    actions_code = """name: Flask App CI/CD Pipeline
on:
  push:
    branches: [ "main", "staging" ]
    tags: [ "v*.*.*" ]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.10", cache: "pip" }
      - run: |
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest --disable-warnings -v
  deploy-staging:
    needs: test
    if: github.ref == 'refs/heads/staging' && github.event_name == 'push'
    runs-on: ubuntu-latest
    steps:
      - uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.STAGING_HOST }}
          username: ${{ secrets.STAGING_USER }}
          key: ${{ secrets.STAGING_SSH_KEY }}
          script: cd /var/www/flask_app && git pull origin staging && sudo systemctl restart flask-staging.service
  deploy-production:
    needs: test
    if: startsWith(github.ref, 'refs/tags/v')
    runs-on: ubuntu-latest
    steps:
      - uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.PROD_HOST }}
          username: ${{ secrets.PROD_USER }}
          key: ${{ secrets.PROD_SSH_KEY }}
          script: cd /var/www/flask_app && git fetch --tags && git checkout ${{ github.ref_name }} && sudo systemctl restart flask-prod.service"""

    t_actions = Table([[Preformatted(actions_code, code_style)]], colWidths=[540])
    t_actions.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EDF2F7")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_actions)
    story.append(Spacer(1, 10))

    # SECTION 3: Application Screenshots Walkthrough
    story.append(Paragraph("3. Application Operational Verification & Screenshots", h1_style))
    story.append(Paragraph(
        "Screenshots tracking the deployment validation and core features of the Student Registration application:",
        body_style
    ))
    story.append(Spacer(1, 6))

    screenshots = [
        ("1. Initial Home Screen", "screenshots/01_home_initial.png"),
        ("2. Student Registration Form (Add Student)", "screenshots/02_add_student.png"),
        ("3. Home Screen (Record Added Verification)", "screenshots/03_home_added.png"),
        ("4. Update Student Form", "screenshots/04_update_student.png"),
        ("5. Home Screen (Record Modification Completed)", "screenshots/05_home_updated.png")
    ]

    for label, img_path in screenshots:
        step_elements = []
        step_elements.append(Paragraph(f"<b>{label}</b>", h2_style))
        if os.path.exists(img_path):
            step_elements.append(Image(img_path, width=510, height=215))
        else:
            step_elements.append(Paragraph(f"<i>[Image file not found: {img_path}]</i>", body_style))
        step_elements.append(Spacer(1, 6))
        story.append(KeepTogether(step_elements))

    doc.build(story)
    print(f"Generated PDF: {filename}")

if __name__ == "__main__":
    build_pdf()
```