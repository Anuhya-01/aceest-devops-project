# ACEest Fitness & Gym – CI/CD DevOps Project

## 1. Project Overview

This project demonstrates a complete CI/CD pipeline using Flask, GitHub Actions, Docker, and Pytest.

The pipeline automates:
- Code integration  
- Testing  
- Docker image creation  

This ensures faster, reliable, and consistent application delivery.

---

## 2. Tools & Technologies Used

The following tools and technologies were used in this project:
- **Python** → Backend programming  
- **Flask** → Web framework  
- **GitHub** → Version control  
- **Pytest** → Testing framework  
- **Docker** → Containerization  
- **GitHub Actions** → CI/CD automation  
- **Jenkins** → Build tool (conceptual)

---

## 3. Project Structure
aceest-devops/

│

├── .github/
    └── workflows/
        └── main.yml        # CI/CD pipeline

├── Dockerfile              # Container configuration

├── README.md               # Documentation

├── app.py                   # Flask application

├── requirements.txt        # Dependencies

├── test_app.py             # Pytest test cases


![Project Structure](GitStructure.png)


---

## 4. Run Application Locally

Follow these steps to run the application on your local machine:
### Step 1: Install dependencies
pip install -r requirements.txt
### Step 2: Run the application
python app.py
### Step 3: Open in browser
http://127.0.0.1:5000  

The following screenshots shows the Installation & Flask application running successfully in the browser: 

![Browser Output](Pyrun.png)

![Browser Output](Pybrows.png)


---

## 5. Run Tests

Execute the following command to run test cases:

python -m pytest

### Expected Output:
`2 passed`

## 5.1 Test Output

The following screenshot shows successful execution of test cases:

![Pytest Result](Pytest.png)


---

## 6. Docker Setup
Docker is used to containerize the application for consistent deployment across environments.
### 6.1 Build Docker Image
docker build -t aceest-app .
### 6.2 Run Docker Container
docker run -p 5000:5000 aceest-app

![Browser Output](Docker_Build_Run.png)

### 6.3 Access Application
http://localhost:5000

## 6.4 Docker Output

The following screenshot shows the application running inside a Docker container:

![Docker Output](Docker.png)

---
## 7. CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is implemented using GitHub Actions and is defined in:

.github/workflows/main.yml

### 7.1 Pipeline Workflow:

1. Code is pushed to GitHub repository  
2. GitHub Actions workflow is triggered automatically  
3. Dependencies are installed  
4. Test cases are executed using Pytest  
5. Docker image is built  

This automation ensures that the application is always tested and ready for deployment.

---

## 7.2 CI/CD Pipeline Result

The following screenshot shows successful execution of the CI/CD pipeline:
![CI/CD Pipeline](Action.png)

---

## 8. Architecture Diagram

The architecture of the system follows a CI/CD pipeline approach:
Developer → GitHub → GitHub Actions → Pytest → Docker → Application Deployment

This improves:
- Development speed  
- Code quality  
- Deployment reliability
  
![Architecture](Architecture.png)

---

## 9. Jenkins Integration

Jenkins is a build automation tool used for continuous integration.

In this project:
- GitHub Actions is used as the primary CI/CD tool  
- Jenkins is considered as an additional validation tool  

---

## 🔧 Jenkins Integration

Jenkins is used as an additional Continuous Integration (CI) tool to validate the application build and testing process.

### 🔹 Purpose
- Acts as a secondary validation layer
- Ensures code builds successfully
- Verifies test execution independently from GitHub Actions

### 🔹 Jenkins Workflow
1. Pulls source code from GitHub repository  
2. Executes build process  
3. Installs dependencies  
4. Runs test cases using Pytest  
5. Displays build status (Success/Failure)

### 🔹 Configuration Details
- Source Code: GitHub Repository  
- Branch: main  
- Build Tool: Execute Shell  
- Test Framework: Pytest  

### 🔹 Outcome
- Jenkins successfully triggers builds  
- Validates application functionality  
- Provides an additional quality gate in CI/CD pipeline  

---

## 📸 Jenkins Build Screenshots

### ✅ Build Triggered
![Build Trigger](Build_Run.png)

### 🔗 Repository Connected
![GitHub Integration](Jerkin connected to Github.png)

### 📊 Build Status
![Build Status](Build Schedule.png)

---

## 10. Conclusion

This project demonstrates a complete DevOps pipeline that automates:
- Code integration  
- Testing  
- Containerization  

This improves efficiency, reliability, and deployment speed.



