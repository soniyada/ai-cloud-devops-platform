# AI-Powered Cloud Deployment Platform

## Overview
A machine-learning sentiment analysis API deployed on AWS using Docker and Terraform. The project demonstrates cloud infrastructure provisioning, application containerization, automated testing, and CI workflows.

## Architecture
- **Application:** Python, FastAPI, scikit-learn
- **Cloud:** AWS EC2, VPC, subnet, Internet Gateway, security group
- **Infrastructure as Code:** Terraform
- **Containerization:** Docker
- **CI:** GitHub Actions
- **Web server:** Nginx

## Features
- Text sentiment prediction API
- Health check endpoint
- Interactive API documentation
- Dockerized application
- Automated tests and container image build
- Repeatable AWS infrastructure deployment

## Run locally
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs.

## Run tests
```powershell
python -m pytest -q
```

## Docker
```powershell
docker build -t ai-cloud-platform:1.0 .
docker run --rm -p 8000:8000 ai-cloud-platform:1.0
```

## Deployment
```powershell
cd terraform
copy terraform.tfvars.example terraform.tfvars   # then edit values
terraform init
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
```
The configuration provisions AWS networking and an EC2 instance. The instance installs Docker and Nginx, builds the application image, and serves the API through Nginx. Review AWS pricing and permissions before deployment.

## Cleanup
```powershell
terraform destroy
```

## Limitations and future improvements
- Train and evaluate the model on a larger labeled dataset.
- Add HTTPS and a custom domain.
- Add an Application Load Balancer and Auto Scaling.
- Add centralized logging, metrics, and alerts.
- Implement secure CI/CD deployment with short-lived AWS credentials.
- Add model versioning and monitoring.

## Author
Add your name, GitHub profile, and LinkedIn profile here.
