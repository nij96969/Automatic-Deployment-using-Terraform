import os
from dotenv import load_dotenv
from mail import send_email
import json
# Load environment variables from the .env file
load_dotenv()

# Set working directory
os.chdir("D:/Terraform")
print(os.getcwd())

# Terraform configuration file
config_file = "ec_instance.tf"

# Set environment variables for authentication
os.environ["SENDER_MAIL"] = os.getenv("sender_mail")
os.environ["RECEIVER_EMAIL"] = os.getenv("receiver_email")
os.environ["SENDER_APP_PASSWORD"] = os.getenv("sender_app_password")
os.environ["ACCESS_KEY"] = os.getenv("access_key")
os.environ["SECRET_KEY"] = os.getenv("secret_key")

# Read terraform.tfstate.backup
file_path = r"D:\Terraform_Automation\terraform.tfstate.backup"
with open(file_path, 'r') as file:
        data = json.load(file)

# Cpoy the Private Key to deployer-key.pem which can be used to send to client 
private_key = data['outputs']['private_key_pem']['value']
with open("deployer-key.pem", "w") as key_file:
    key_file.write(private_key)

# Private Key Name
key_file_name = "deployer-key.pem"

# Obtain the instance public DNS
print("Obtaining the instance public DNS...")
instance_public_dns = data['outputs']['instance_public_dns']['value']

# Construct the SSH command
ssh_command = f'ssh -i "{key_file_name}" ubuntu@{instance_public_dns}'

print(ssh_command)

# Retrieve email credentials
sender_email = os.getenv("SENDER_MAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
sender_app_password = os.getenv("SENDER_APP_PASSWORD")

subject = 'File Attachment Test'
body = f"TO conncet to EC2 instance Download the Key Pair and use SSH Command in terminal :: {ssh_command}"
attachment_path = r'D:\Terraform\deployer-key.pem'  # Change this to the path of your file

send_email(sender_email, sender_app_password, receiver_email, subject, body, attachment_path)