# 🏋️ ACEest Fitness & Gym – CI/CD DevOps Project

## 🚀 Project Overview

This project demonstrates a complete CI/CD pipeline using Flask, GitHub Actions, Docker, and Pytest.

The pipeline automates:
- Code integration  
- Testing  
- Docker image creation  

This ensures faster, reliable, and consistent application delivery.

---

## 🧰 Tools & Technologies Used

The following tools and technologies were used in this project:
- **Python** → Backend programming  
- **Flask** → Web framework  
- **GitHub** → Version control  
- **Pytest** → Testing framework  
- **Docker** → Containerization  
- **GitHub Actions** → CI/CD automation  
- **Jenkins** → Build tool (conceptual)

---

## 📁 Project Structure

![Project Structure](GitStructure.png)


---

## ⚙️ Run Application Locally

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

## 🧪 Run Tests

Execute the following command to run test cases:
python -m pytest

### Expected Output:
`2 passed`

## 🧪 Test Output

The following screenshot shows successful execution of test cases:

![Pytest Result](Pytest.png)


---

## 🐳 Docker Setup
Docker is used to containerize the application for consistent deployment across environments.
### Build Docker Image
docker build -t aceest-app .
### Run Docker Container
docker run -p 5000:5000 aceest-app

![Browser Output](Docker_Build_Run.png)

### Access Application
http://localhost:5000

## 📸 Docker Output

The following screenshot shows the application running inside a Docker container:

![Docker Output](Docker.png)

---
## ⚙️ CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is implemented using GitHub Actions and is defined in:

.github/workflows/main.yml

### 🔄 Pipeline Workflow:

1. Code is pushed to GitHub repository  
2. GitHub Actions workflow is triggered automatically  
3. Dependencies are installed  
4. Test cases are executed using Pytest  
5. Docker image is built  

This automation ensures that the application is always tested and ready for deployment.

---

## 📸 CI/CD Pipeline Result

The following screenshot shows successful execution of the CI/CD pipeline:
![CI/CD Pipeline](Action.png)

---

## 🏗️ Architecture Diagram

The architecture of the system follows a CI/CD pipeline approach:
Developer → GitHub → GitHub Actions → Pytest → Docker → Application Deployment

This improves:
- Development speed  
- Code quality  
- Deployment reliability
  
![Architecture](Architecture.png)

---

## 🔧 Jenkins Integration

Jenkins is a build automation tool used for continuous integration.

In this project:
- GitHub Actions is used as the primary CI/CD tool  
- Jenkins is considered as an additional validation tool  

### Jenkins Workflow:
- Pull code from GitHub  
- Execute build and tests  
- Validate application  

---

## 📌 Conclusion

This project demonstrates a complete DevOps pipeline that automates:
- Code integration  
- Testing  
- Containerization  

This improves efficiency, reliability, and deployment speed.



