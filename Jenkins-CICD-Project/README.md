# 🚀 Jenkins CI/CD Pipeline with Docker, SonarQube, and Argo CD  

This project demonstrates a **complete CI/CD pipeline** using **Jenkins**, **SonarQube**, **Maven**, **Docker**, and **Argo CD** for continuous integration, automated testing, containerization, and deployment to a **Kubernetes cluster**.

---

## 🧩 Pipeline Overview

The pipeline automates every stage of the software development lifecycle — from code commit to production deployment.

### 🔁 Workflow Steps

1. **Source Code Commit**
   - Developer pushes the latest code to a Git repository (e.g., GitHub).
   - A **webhook** triggers Jenkins to start the build process.

2. **Build Stage (Maven)**
   - Jenkins pulls the source code and builds the project using **Maven**.
   - The build artifacts (like `.jar` files) are generated.

3. **Static Code Analysis (SonarQube)**
   - Jenkins runs **SonarQube** to analyze the code for bugs, code smells, and security vulnerabilities.
   - If the code passes SonarQube quality gates, the pipeline continues.

4. **Testing**
   - Automated unit tests are executed.
   - If tests fail, Jenkins stops the pipeline and notifies the team via **Slack** or **Email**.

5. **Docker Build and Push**
   - A **Docker image** is built from the application and pushed to **DockerHub** (or another container registry).

6. **Image Updater**
   - A script automatically updates the **Kubernetes manifests** with the new Docker image tag.

7. **Continuous Deployment (Argo CD)**
   - **Argo CD** continuously monitors the manifests repository.
   - On detecting updates, it deploys the latest image to the **Kubernetes cluster** automatically.

---

## 🧰 Tech Stack

| Category | Tools |
|-----------|-------|
| **CI/CD Tool** | Jenkins |
| **Build Tool** | Maven |
| **Code Quality** | SonarQube |
| **Containerization** | Docker |
| **Registry** | DockerHub |
| **Deployment** | Argo CD |
| **Orchestration** | Kubernetes |
| **Version Control** | GitHub |

---

## ⚙️ Features

- Automated **build → test → deploy** pipeline  
- **Static code analysis** with SonarQube  
- **Containerization** using Docker  
- **GitOps-style deployment** using Argo CD  
- **Real-time notifications** via Slack and Email  
- Fully integrated **DevSecOps workflow**

---

## ⚡ How the Pipeline Works

1. **Code Push → Webhook → Jenkins Build Trigger**
2. **Builds & Tests → Maven**
3. **Code Analysis → SonarQube**
4. **Container Build & Push → DockerHub**
5. **Manifest Update → GitHub Repo**
6. **Deployment → Argo CD → Kubernetes**
7. **Notifications → Slack / Email**

---

## 🧠 Learning Outcomes

Through this project, you will learn to:
- Design a **complete CI/CD pipeline** using Jenkins  
- Integrate **SonarQube** for static code analysis  
- Automate **Docker image creation and pushing**  
- Deploy applications automatically with **Argo CD**  
- Monitor deployment pipelines with **Slack notifications**

---

## 🔒 Security Highlights
- Secrets and credentials are stored securely in Jenkins credentials store.  
- DockerHub access tokens and Kubernetes credentials are never exposed in plain text.  
- Quality gates ensure no vulnerable code reaches production.

---

## 🌐 Deployment Flow

```text
Developer → GitHub → Jenkins → SonarQube → DockerHub → Argo CD → Kubernetes

🧑‍💻 Author

Gokul K

📫 Connect: LinkedIn| GitHub

🏁 Conclusion

This project showcases a modern CI/CD setup that integrates continuous integration, automated testing, containerization, and GitOps-based deployment ensuring faster, more reliable, and secure software delivery.
