# CloudOps CLI ☁️

An AWS resource manager CLI for LocalStack/Moto, built for DevOps automation.

## 📦 Installation

```bash
git clone https://github.com/2nothing4/cloudops-cli.git
cd cloudops-cli
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
Windows Setup
Install Git and Python (check "Add python.exe to PATH").

If venv activation is blocked, run:

powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Create and activate the venv:

powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
## 🚀 Usage
Start a mock AWS backend in a separate terminal (keep it running):

bash
pip install "moto[server]"
moto_server -p 4566
Check health:

bash
cloudops health
List S3 buckets:

bash
cloudops s3-list
EC2 Commands:

bash
# Create instance
cloudops ec2-create --name my-server

# List instances
cloudops ec2-list

# Terminate instance
cloudops ec2-terminate i-xxxxxxxx
## 🏗️ Infrastructure as Code (Terraform)
Deploy an EC2 instance to LocalStack/Moto:

bash
cd terraform
terraform init
terraform apply -auto-approve
## 🛠️ Tech Stack
Python 3.12+

boto3 (AWS SDK)

click (CLI framework)

moto (AWS mocking)

## 🧪 Testing
(Coming soon: Add instructions on how to run your pytest suite here).

Author
Ziad — GitHub Profile
