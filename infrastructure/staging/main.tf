provider "google" {
  project     = var.gcp-project-id
  region      = var.gcp-region
  zone        = var.gcp-zone
  credentials = "keys.json"
}

terraform {
  backend "gcs" {
    bucket = "terraform-state-gorgias-sre-assessment"
    credentials = "keys.json"
    prefix = "terraform/staging/state"
  }
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

module "vpc" {
  source         = "../modules/vpc"
  gcp-project-id = var.gcp-project-id
  gcp-region     = var.gcp-region
}

module "k8s-cluster" {
  source                 = "../modules/k8s"
  depends_on             = [module.vpc]
  k8s-network            = module.vpc.network
  k8s-subnetwork         = module.vpc.subnetwork
  gcp-project-id         = var.gcp-project-id
  gke-cluster-name       = var.gke-cluster-name
  master-ipv4-cidr-block = "172.16.0.0/28"
}
