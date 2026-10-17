variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "ap-south-1"
}

variable "project_name" {
  description = "Resource name prefix"
  type        = string
  default     = "ai-cloud-devops"
}

variable "my_ip" {
  description = "Your public IPv4 address with /32 suffix"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "repo_url" {
  description = "Public HTTPS URL of your GitHub project"
  type        = string
}
