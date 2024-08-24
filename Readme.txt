The Basic command to run terraform / in our case we are using it to set up the EC2 instance  

terraform init
terraform apply

The reason These are not being executed using python because we wont be able to destroy the EC2 instace when needed
The files that terraform generates when being executed by python won't be stored in the local directory
This is reason why terraform commands are being executed manually

Once the terraform apply is performed You have send the credentials to the Client/User 
Thus Send_Credential.py a python file will be executed 

Send_Credential reads the terraform.tfstate.backup to obtain the DNS name and the private_key_pem which will be send to Client/user_data

in .env file you have mention the sender mail , receiver mail , snder_app_password that can be generated using link provided in the mail.py

in variables mention the required variables such as aws_access_key and aws_secret_key
and store the aws_access_key and aws_secret_key in terraform.tfvars just like as we store in .env file
refer terraform documentaion for storing variables