output "public_ip" {
  description = "Public IP address of the application server"
  value       = aws_instance.app.public_ip
}

output "application_url" {
  description = "URL of the deployed application"
  value       = "http://${aws_instance.app.public_ip}"
}
