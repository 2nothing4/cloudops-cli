<div align="center">☁️ CloudOps CLI
Local-first AWS automation from your terminal.
A Python CLI for selected AWS resource operations, built with boto3 and Click and designed to be exercised against a local AWS-compatible emulator such as Moto.
<p>
  <img src="https://img.shields.io/badge/Python-CLI-3776AB?logo=python&logoColor=white" alt="Python CLI" />
  <img src="https://img.shields.io/badge/AWS-boto3-FF9900?logo=amazonaws&logoColor=white" alt="AWS boto3" />
  <img src="https://img.shields.io/badge/CLI-Click-111111" alt="Click CLI" />
  <img src="https://img.shields.io/badge/Local%20testing-Moto-5B8C5A" alt="Moto local testing" />
  <img src="https://img.shields.io/badge/IaC-Terraform-7B42BC?logo=terraform&logoColor=white" alt="Terraform" />
  <img src="https://img.shields.io/badge/Status-Active%20development-orange" alt="Active development" />
</p>
A hands-on DevOps automation project by Ziad.
</div>✨ What is CloudOps CLI?
CloudOps CLI brings a small set of cloud operations into one command-line interface. It uses boto3 to make AWS API calls and can be configured for local development against an AWS-compatible endpoint.
[!IMPORTANT]
Project scope: this is a personal DevOps automation project in active development. The documented workflow is intended for local development and testing. It is not presented as a production AWS management tool.

⚡ What can it do today?
Command	Operation
cloudops health	Check connectivity to the configured local AWS emulator.
cloudops s3-list	List S3 buckets visible to the configured endpoint.
cloudops ec2-create --name <name>	Create an EC2 instance using the configured endpoint.
cloudops ec2-list	List EC2 instances visible to the configured endpoint.
cloudops ec2-terminate <instance-id>	Request termination of the specified instance.


The repository also includes a Terraform configuration intended to provision an EC2 instance against a local AWS-compatible endpoint. Its behavior depends on the provider configuration and the API operations supported by the selected emulator.
🧭 How the local workflow fits together
```mermaid
flowchart LR
    U[You in the terminal] --> C[CloudOps CLI]
    C --> B[boto3]
    B -->|AWS API requests| M[Moto server\n127.0.0.1:4566]
    M --> S[(Emulated AWS services)]
    T[Terraform configuration] -->|Provider requests| M
```
CloudOps CLI and Terraform are separate clients of the local emulator. Both must be configured to use the intended endpoint; starting Moto alone does not automatically configure either client.
🚀 Quick start
1. Clone the repository
git clone https://github.com/2nothing4/cloudops-cli.git
cd cloudops-cli
2. Create an environment and install the CLI
Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install "moto[server]"
Windows · PowerShell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install "moto[server]"
If PowerShell blocks activation, allow it for the current process only, then activate the environment again:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
The editable install (pip install -e .) installs the CLI and the dependencies declared by this project. Moto server mode is installed separately for the local emulator workflow shown here.
3. Start Moto
In a terminal with the virtual environment activated, start Moto on the loopback interface:
moto_server -H 127.0.0.1 -p 4566
Leave that process running. Open a second terminal, activate the same virtual environment, and continue below.
[!NOTE]
Make sure the CLI's boto3 client is configured to use http://127.0.0.1:4566. Check the endpoint configuration in the application source. Do not assume the CLI is connected to Moto just because the Moto process is running.

4. Run the CLI
# Check the emulator connection
cloudops health

# List S3 buckets
cloudops s3-list

# Create an EC2 instance
cloudops ec2-create --name my-server

# List EC2 instances
cloudops ec2-list
An empty S3 bucket list can be normal when the emulator has not been initialized with any buckets.
5. Terminate the test instance
Use an instance ID returned by cloudops ec2-list:
cloudops ec2-terminate i-xxxxxxxx
[!WARNING]
Termination is a destructive operation. Before running it, confirm that the CLI is targeting your local emulator and that the instance ID belongs to the test environment you intend to clean up.

🏗️ Infrastructure as Code
The terraform/ directory contains an EC2-oriented Terraform configuration intended for a local AWS-compatible endpoint.

Before applying it:
1. Inspect the AWS provider configuration and verify the EC2 endpoint.
2. Confirm that the configuration uses local test credentials—not real AWS credentials.
3. Check that the selected emulator supports the resources and API calls used by the configuration.
4. Never assume that a configuration tested against one emulator will work unchanged against another.
From the repository root:
cd terraform
terraform fmt -check
terraform init
terraform validate
terraform plan
Review the plan carefully. Apply only after verifying that it targets the intended local emulator:
terraform apply
When the test is complete, review and remove the test infrastructure:
terraform plan -destroy
terraform destroy
Do not use -auto-approve for this workflow. Inspecting the plan is part of the safety check.
🧪 Testing & validation
The current documented workflow uses manual local smoke checks. This README does not claim that an automated pytest suite is available.
Check	Expected result
Start Moto on 127.0.0.1:4566	The local emulator starts and remains running.
cloudops health	Reports a successful connection to the configured endpoint.
cloudops s3-list	Returns successfully; an empty list is acceptable for a new emulator.
cloudops ec2-create --name my-server	Creates a test instance in the configured emulator.
cloudops ec2-list	Shows the test instance.
cloudops ec2-terminate <instance-id>	Terminates the test instance; a subsequent list should no longer show it.
Terraform validation	fmt, init, validate and plan complete against the intended configuration.


Automated unit and integration tests, together with a documented test command, should be added when the test suite and development dependencies are present in the repository.
🧰 Technology
Tool	Role
Python	CLI implementation
Click	Command-line interface framework
boto3	AWS SDK for Python
Moto	AWS service mocking and local server mode
Terraform	Infrastructure as Code for the EC2 example


🔐 Security & safe usage
- Use local test credentials with an emulator. Never commit real AWS access keys, secret keys, tokens or credential files.
- Keep Moto bound to 127.0.0.1 for local-only use. Do not expose an unauthenticated emulator to an untrusted network.
- Verify the configured endpoint before creating or terminating resources.
- Treat Terraform state files and saved plan files as potentially sensitive. Keep them out of Git unless there is a deliberate, reviewed reason to publish a sanitized example.
- Do not run the example Terraform configuration against a real AWS account without adapting and reviewing the configuration first.
📍 Current scope & limitations
- The documented CLI command set is limited to the S3 and EC2 operations listed above, plus the health check.
- The documented workflow is for local development and testing; no production AWS deployment is claimed.
- Automated test coverage is not documented as available yet.
- Terraform behavior depends on its provider configuration and the selected emulator's API compatibility.
- The project is under active development; commands and configuration may evolve.
📚 References
- Moto server mode
- boto3 documentation
- Click documentation
- Terraform AWS Provider documentation
<div align="center">Built by Ziad · Repository

Learning by building. Automating one operation at a time.
</div>
