terraform {
  required_version = ">= 1.6.0"
  backend "s3" {}
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "../../modules/vpc"
  name   = "finpilot-stage-vpc"
  cidr   = "10.10.0.0/16"
}

# Extend with subnets, NAT, EKS, ECR, RDS, S3, IAM, and Secrets.
