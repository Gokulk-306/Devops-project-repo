# 🧩 Kubernetes PR Analyzer

A simple Python script that fetches and analyzes pull requests from the official **Kubernetes** GitHub repository.

## 📘 Overview
This project uses the GitHub REST API to:
- Retrieve open pull requests from the Kubernetes repository  
- Count how many pull requests were created by each contributor  
- Display the results in a clean, readable format

## ⚙️ Tech Stack
- **Python 3**
- **Requests library**
- **GitHub REST API**

## 🚀 How It Works
1. Sends a GET request to the Kubernetes pull requests API endpoint.  
2. Extracts pull request data from the JSON response.  
3. Groups PRs by their creator and counts how many each user has opened.  
4. Prints the results in the console.
