variable "gcp-project-id" {
  type = string
}

variable "gke-cluster-name" {
  type = string
}

variable "k8s-network" {
  type = any
}

variable "k8s-subnetwork" {
  type = any
}

variable "master-ipv4-cidr-block" {
  type = string
}

