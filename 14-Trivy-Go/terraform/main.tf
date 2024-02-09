# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html

# Launch an EC2 instance
resource "aws_instance" "web" {
  ami           = var.ami # Ubuntu Server 20.04 LTS
  instance_type = var.instance_type

  key_name        = "ansible"
  security_groups = ["allow_ssh_http_new_sg"]
  
  tags = {
    Name        = "webserver"
    Environment = "dev"
  }
}

output "publicIP" {
  value = aws_instance.web.public_ip
}
