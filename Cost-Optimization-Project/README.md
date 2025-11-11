# 💰 AWS Cost Optimization – Automated EBS Snapshot Cleanup with Lambda  

This project demonstrates an **AWS cost optimization solution** using **AWS Lambda** and **Boto3** to automatically identify and delete **unused EBS snapshots**, reducing unnecessary storage costs.  

The Lambda function intelligently scans for **stale or unattached EBS snapshots** and removes them to maintain an efficient and cost-effective cloud environment.  

---

## 🧩 Project Overview  

AWS environments often accumulate unused **EBS snapshots** over time — for example, when EC2 instances or volumes are deleted without cleaning up related snapshots.  
This script ensures that only relevant, attached snapshots are retained while **automatically deleting orphaned ones**, optimizing AWS storage costs.  

---

## 🔁 Workflow Steps  

1. **List All Snapshots**  
   - The Lambda function retrieves all **EBS snapshots** owned by your AWS account.  

2. **Get Active EC2 Instances**  
   - Lists all **currently running EC2 instances** to identify active resources.  

3. **Filter Unused Snapshots**  
   - For each snapshot:
     - If it’s not linked to any **EBS volume**, it’s deleted.  
     - If its associated volume no longer exists or isn’t attached to any **running instance**, it’s also deleted.  

4. **Snapshot Deletion**  
   - The function uses `delete_snapshot()` to remove identified unused snapshots.  
   - Each deletion is logged with a clear message for audit and monitoring.  

---

## 🧰 Tech Stack  

| Category | Tools/Services |
|-----------|----------------|
| **Cloud Provider** | AWS |
| **Compute** | AWS Lambda |
| **SDK** | Boto3 (Python SDK for AWS) |
| **Service Managed** | Amazon EC2, Amazon EBS |
| **Language** | Python |

---

## ⚙️ Features  

- ✅ Automatically detects **orphaned EBS snapshots**  
- 🧹 Deletes **snapshots not linked to active volumes or instances**  
- 💸 Helps **reduce AWS storage costs**  
- 🔐 Secure operation using **IAM Roles** and **AWS Credentials Store**  
- ☁️ **Serverless** implementation – runs periodically without manual intervention  

---

## 🧠 Learning Outcomes  

Through this project, you will learn to:  
- Integrate **AWS Lambda** with **EC2 and EBS APIs** using Boto3  
- Automate **cloud resource cleanup** workflows  
- Apply **cost optimization strategies** in AWS environments  
- Implement **serverless automation** with scheduled triggers  
- Manage **IAM permissions** securely for Lambda functions  

---

## 🔒 Security Highlights  

- Uses **IAM Role-based Access Control (RBAC)** for Lambda permissions  
- Restricts access to `DescribeSnapshots`, `DescribeVolumes`, and `DeleteSnapshot` actions only  
- No hardcoded credentials — relies on AWS’s secure credentials management  
- Detailed logging for traceability and auditing in **CloudWatch Logs**  

---

## ⚡ Architecture Flow  

```text
CloudWatch Event (Trigger)
        ↓
AWS Lambda (Python Script)
        ↓
Boto3 interacts with EC2 & EBS APIs
        ↓
Identifies unused snapshots
        ↓
Deletes unneeded snapshots
        ↓
Logs actions to CloudWatch
