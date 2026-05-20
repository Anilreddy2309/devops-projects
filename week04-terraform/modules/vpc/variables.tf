variable "name" {
  description = "Name prefix for all resources"
  type        = string
}

variable "cidr" {
  description = "CIDR block for the VPC e.g. 10.0.0.0/16"
  type        = string
}

variable "public_subnets" {
  description = "List of public subnet CIDR blocks"
  type        = list(string)
}

variable "azs" {
  description = "List of availability zones"
  type        = list(string)
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {}
}
