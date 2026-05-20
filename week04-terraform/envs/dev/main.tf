# This file uses the VPC module to create a real VPC in AWS
# Think of modules like functions — define once, use many times

module "vpc" {
  source = "../../modules/vpc"

  name           = "devops-dev"
  cidr           = "10.0.0.0/16"
  public_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  azs            = ["us-east-1a", "us-east-1b"]

  tags = {
    Environment = "dev"
    Project     = "devops-portfolio"
    Owner       = "anil"
  }
}

output "vpc_id" {
  value = module.vpc.vpc_id
}

output "subnet_ids" {
  value = module.vpc.public_subnet_ids
}
