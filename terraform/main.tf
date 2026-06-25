provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    ec2 = "http://localhost:4566"
  }
}

resource "aws_instance" "ziad_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  tags = {
    Name = "ziad-server"
  }
}
