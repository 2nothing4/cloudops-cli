# CloudOps CLI

AWS resource manager for LocalStack/Moto. DevOps automation tool.

## Install

```bash
git clone https://github.com/2nothing4/cloudops-cli.git
cd cloudops-cli
python3 -m venv venv
source venv/bin/activate
pip install -e .
```
### Windows

1. Install [Git](https://git-scm.com/download/win) and [Python](https://www.python.org/downloads/)
   (check **"Add python.exe to PATH"** during Python setup).
2. If venv activation is blocked, run once:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
3. Create and activate the venv — always confirm the `(venv)` prompt
   marker before running `pip install`:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Start a mock AWS backend in a second terminal (leave it running):
   ```powershell
   pip install "moto[server]"
   moto_server -p 4566
   ```
5. `cloudops health` should print `Moto: OK`

## Usage

Start Moto (AWS mock server):
```bash
moto_server -p 4566
```

Check health:
```bash
cloudops health
```

List S3 buckets:
```bash
cloudops s3-list
```

## Tech Stack
- Python 3.14
- boto3
- click
- moto (for testing)

## Author
Ziad — DevOps 180

## EC2 Commands

Create instance:
```bash
cloudops ec2-create --name my-server
```

List instances:
```bash
cloudops ec2-list
```

Terminate instance:
```bash
cloudops ec2-terminate i-xxxxxxxx
```

## Infrastructure as Code (Terraform)

Deploy EC2 instance to LocalStack/Moto:

```bash
cd terraform
terraform init
terraform apply -auto-approve
