# gorgias-sre-assessment
A simple flask application deployed on GKE

## Tech stack

- Flask web application with semantic release & versioning
- Postgres database deployed using Helm & Github actions
- Infrastructure provisioned with Terraform on GCP
- Docker-compose setup for local development & testing
- Github actions for CI/CD:
  - Linting & semantic release
  - Package, build & push Docker images
  - Deploys flask app
  - Deploys postgres
  - Deploys an ingress controller


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


## Connecting to GKE cluster using CLI

- Install the gcloud cli tooling & kubectl using the [official documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
- Authenticate using the gke-gcloud-auth-plugin
- Finally, get the credentials using:
  ```
  gcloud container clusters get-credentials gorgias-sre-assessment --zone us-central1-a --project bubbly-sentinel-416701
  ```

## Accessing the flask application from a browser
- Add the following entry to `/etc/hosts`
  ```
  34.42.92.122 webapp.gorgias.com
  ```
- On the browser, access the application using [webapp.gorgias.com](http://webapp.gorgias.com)
