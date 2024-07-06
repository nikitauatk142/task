Flask aplication
=========

This installation uses terraform and ansible-playbook for deploy Flask application to AWS EC2

Getting started
---------------
Download and install Terraform https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

Download and install Ansible https://docs.ansible.com/ansible/latde/getting-started-install.html

Download, install and configure AWS CLI https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

Terraform will use default AWS CLI User
# Before start!

This installation olny for linux machine and in aws uses only Amazon linux OS Images (ami-08ca6be1dc85b0e84) in eu-west-1a
For other region you need to change variable "AWS_REGION" and variable "AMIS" in vars.tf


In the repo exist ssh key pair which was created only for this project (mykey and mykey.pub) for example. You can use this pair or create your own.
If you create your key pair you have to update path to it in instance.tf (provisioner block) and variable "PATH_TO_PRIVATE_KEY", variable "PATH_TO_PUBLIC_KEY" in vars.tf
Also this pair using for ansible ssh connection to EC2

# Installation

This installation will create VPC, Subnets, Security group for EC2 and instance (*.tf files), install Nginx, Flask app from app dir by using ansible playbook (playbook.yml)

In app dir check application code /app/application.py
*.tf - terrform files 
playbook.yml - the ansible playbook contains tasks that are performed when the instance is deployed. Check what every step is doing

**# 1. Clone the project**

**# 2. Run in task directory for initializing a working directory**

```
terraform init
```
**# 3. Run for creating an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure**
```
terraform plan
```
**# 4. Run for executing the actions proposed in a Terraform plan**
```
terraform apply
```
**# 5. In output check your EC2 IP**

Go to http://ec2_ip/hello in browser

Output shoul be "hello prozorro"

**# 6. For delete run:**
```
terraform destroy
```
