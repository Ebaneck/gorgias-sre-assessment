output "network" {
  value       = google_compute_network.main.self_link
  description = ""
}

output "subnetwork" {
  value       = google_compute_subnetwork.private.self_link
  description = ""
}