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
