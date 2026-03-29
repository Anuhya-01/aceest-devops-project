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

- **Python** → Backend programming  
- **Flask** → Web framework  
- **GitHub** → Version control  
- **Pytest** → Testing framework  
- **Docker** → Containerization  
- **GitHub Actions** → CI/CD automation  
- **Jenkins** → Build tool (conceptual)

---

## 📁 Project Structure
aceest-devops/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
└── workflows/
└── main.yml


---

## ⚙️ Run Application Locally
pip install -r requirements.txt
python app.py

Open in browser:  
http://127.0.0.1:5000

---

## 🧪 Run Tests
python -m pytest

Expected Output:  
`2 passed`

---

## 🐳 Docker Setup
docker build -t aceest-app .
docker run -p 5000:5000 aceest-app


Open:  
http://localhost:5000

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is defined in:


.github/workflows/main.yml


### 🔄 Pipeline Workflow:
1. Code push triggers pipeline  
2. Dependencies are installed  
3. Tests are executed using Pytest  
4. Docker image is built  

---

## 📸 CI/CD Pipeline Result



---

## 🏗️ Architecture Diagram

## 🐳 Docker Output



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



