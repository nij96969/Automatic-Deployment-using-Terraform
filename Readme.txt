This Project aims to automate the deployment process of web applications using Jenkins Pipeline 

Jenkins Pipeline is automatically setup in EC2 and its steps are mentioned in user_data.sh which is not uploaded on the current repository due to important credentials required for setup of the project mentioned later on.

The required downloading and setup happens in my case i am automating the deployment of LLM Based Docker Generator and Automation (flask_app)

Overview of the user_data.sh is provided to refer the flow of setup

The Basic command to run terraform / in our case we are using it to set up the EC2 instance  

terraform init
terraform apply

Once the terraform apply is performed You have send the credentials to the Client/User 
Thus Send_Credential.py a python file will be executed 

Send_Credential reads the terraform.tfstate.backup to obtain the DNS name and the private_key_pem which will be send to Client/user_data

in .env file you have mention the sender mail , receiver mail , snder_app_password that can be generated using link provided in the mail.py

in variables mention the required variables such as aws_access_key and aws_secret_key
and store the aws_access_key and aws_secret_key in terraform.tfvars just like as we store in .env file
refer terraform documentaion for storing variables
