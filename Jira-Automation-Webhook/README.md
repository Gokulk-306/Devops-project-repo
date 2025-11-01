# Jira Automation Webhook

This project automates Jira ticket creation using a Flask-based REST API that listens for GitHub issue comments.

## 📘 Overview
When a user comments `/jira` on a GitHub issue, the Flask service receives the webhook event and automatically creates a Jira ticket using the Jira REST API.

## ⚙️ Tech Stack
- **Flask** – Web framework for building REST API  
- **Requests** – For interacting with Jira REST API  
- **Jira Cloud API** – To create issues programmatically  
- **Environment Variables** – For secure API token management  

## 🚀 How It Works
1. GitHub sends a webhook to `/createJira` endpoint when a comment is made.
2. The Flask app checks if the comment contains `/jira`.
3. If true, a new Jira issue is created under the specified project.