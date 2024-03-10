# gorgias-sre-assessment
A simple flask application deployed on GKE

## Tech stack

- Flask web application with semantic release & versioning
- Postgres database deployed using Helm & Github actions
- Infrastructure provisioned with Terraform on GCP
- Docker-compose setup for local development & testing
- Github actions for CI/CD


## Docker instructions

To create a docker image execute:

`docker build . -t flaskapp`

To run the docker image execute:

`docker run -p 5000:5000 flaskapp` and visit with your browser http://localhost:5000


## GCP Infrastructure

To deploy the infrastructure we need to:

* Create the GCS bucket to store the tf state
* Create an IAM user with a service account & required permissions for terraform
* Enable Service Usage APIs
* Finally use Terraform to plan & apply changes.
