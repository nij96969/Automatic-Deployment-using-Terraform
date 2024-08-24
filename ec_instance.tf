provider "aws" {
  region = "ap-south-1"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = tls_private_key.deployer.public_key_openssh
}

resource "tls_private_key" "deployer" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_instance" "example2" {
  ami           = "ami-0f58b397bc5c1f2e8"  # Ubuntu 20.04 LTS (HVM), SSD Volume Type
  instance_type = "t2.micro"
  security_groups = ["SSH_Http_Https"]  # Use the existing security group named SSH_Http_Https
  key_name = "deployer-key"
  # user_data = file("user_data.sh")

  tags = {
    Name = "Jenkins-Automation-instance-${timestamp()}"  # Adding a timestamp to the instance name
  }
}

output "private_key_pem" {
  value     = tls_private_key.deployer.private_key_pem
  sensitive = true
}

output "instance_public_dns" {
  value = aws_instance.example2.public_dns
}

