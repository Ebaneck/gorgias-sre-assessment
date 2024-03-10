variable "gke-cluster-name" {
  type = string
  default = "gorgias-sre-assessment"
}

variable "gcp-project-id" {
  type = string
  default = "bubbly-sentinel-416701"
}

variable "tfstate-bucket-name" {
  type = string
  default = "terraform-state-gorgias-sre-assessment"
}

variable "gcp-region" {
  type = string
  default = "us-central1"
}

variable "gcp-zone" {
  type = string
  default = "us-central1-a"
}

variable "gcp-auth-file" {
  type        = string
  default = "./keys.json"
}
