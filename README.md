# gorgias-sre-assessment

A simple Todo flask application containerized and deployed on GKE.

## Tech stack

- Flask web application with semantic release & versioning enabled
- Postgres database deployed using Helm & Github actions
- Infrastructure provisioned with Terraform on GCP
- Docker-compose setup for local development & testing
- Github actions for CI/CD:
  - Linting & semantic release
  - Package, build & push Docker images
  - Deploys flask Todo app
  - Deploys postgres as database
  - Deploys an ingress controller

### Rationale behind the tech choices

- Adding Semantic release and versioning brings along consistent and automated version management.

- Helm & Helm charts would simplify the deployment and management of the database and other components.
  
- Terraform allows for infrastructure-as-code, making it easier to provision and manage the required resources on Google Cloud Platform (GCP).

- Docker-compose provides a convenient way to define and run multi-container applications, allowing for easy setup and testing of the application locally.

- Github actions will enable continuous integration and continuous deployment (CI/CD) workflows. The actions perform various tasks such as linting, building and pushing Docker images, and deploying the flask app, postgres, and ingress controller.

The chosen tech stack offers a combination of flexibility, automation, and ease of use, making it suitable for developing and deploying the gorgias-sre-assessment project.

## Repository folder structure

- `.github` contains the Github action workflows for build & deploy
- `flaskapp` contains the source code for the Todo flask application
- `helm-charts` contains custom helm-charts & values files used for deployment
- `infrastructure` contains the terraform code used to provision the vpc, k8s & more

## Docker instructions

To create a docker image locally, execute:

`docker build . -t flaskapp`

## GCP Infrastructure

To deploy the infrastructure we need to:

- Create the GCS bucket to store the tf state
- Create an IAM user with a service account & required permissions for terraform
- Enable Service Usage APIs
- Finally use Terraform to plan & apply changes.

## About the Todo app

### App features and setup

- The flask application is a simple todo list with a PostgreSQL database as the persistent layer. It offers two main features:
  - Ability to create new todo items
  - Ability to list all created todo items
  
### Deploying the flask app

- The flask app is containerized using Docker and deployed using a custom helm-chart located in `/helm-charts/flasksapp-chart`.
- To test the deployment locally, refer to the instructions provided in the [repository](https://github.com/Ebaneck/gorgias-sre-assessment/blob/main/.github/workflows/build-and-deploy-flaskapp.yml#L127).

### Accessing the flask application from a browser

- Add the following entry to `/etc/hosts`

  ```
  34.42.92.122 webapp.gorgias.com
  ```

- On the browser, access the application using [webapp.gorgias.com](http://webapp.gorgias.com)

## Connecting to the DB

### Connecting to the primary DB

- PostgreSQL can be accessed via port `5432` on the following DNS names from within your cluster:

  `postgresql-pg-us1-primary.database.svc.cluster.local - Read/Write connection`

  `postgresql-pg-us1-read.database.svc.cluster.local - Read only connection`

- PostgreSQL service list can be found here:

  ```
  (base) Claudes-MBP$ kubectl get services -n database
  NAME                           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
  postgresql-pg-us1-primary      ClusterIP   10.52.3.7    <none>        5432/TCP   26h
  postgresql-pg-us1-primary-hl   ClusterIP   None         <none>        5432/TCP   26h
  postgresql-pg-us1-read         ClusterIP   10.52.5.54   <none>        5432/TCP   26h
  postgresql-pg-us1-read-hl      ClusterIP   None         <none>        5432/TCP   26h
  ```

- To get the password for "postgres" run:

  ```
  export POSTGRES_ADMIN_PASSWORD=$(kubectl get secret --namespace database postgresql-pg-us1 -o jsonpath="{.data.postgres-password}" | base64 -d)
  ```

- To get the password for the "webapp_user" run:

  ```
  export POSTGRES_PASSWORD=$(kubectl get secret --namespace database postgresql-pg-us1 -o jsonpath="{.data.password}" | base64 -d)
  ```

- To connect to the database run the following command:

  ```
  kubectl run postgresql-pg-us1-client --rm --tty -i --restart='Never' --namespace database --image docker.io/bitnami/postgresql:16.2.0-debian-12-r6 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
    --command -- psql --host postgresql-pg-us1-primary -U webapp_user -d webapp -p 5432
  ```

  ```
  webapp=> \dt
            List of relations
  Schema | Name | Type  |    Owner    
  --------+------+-------+-------------
  public | todo | table | webapp_user
  (1 row)

  webapp=> select * from todo;
  id | title  |           text           |          pub_date          
  ----+--------+--------------------------+----------------------------
    1 | Rocket | Build a rocket like Elon | 2024-03-11 17:44:49.182391
    2 | Gym    | Start weights            | 2024-03-11 18:00:15.24868
  (2 rows)
  ```

- To confirm that streaming replication works:

  ```
  webapp=# select * from pg_stat_replication;
  -[ RECORD 1 ]----+------------------------------
  pid              | 258
  usesysid         | 16386
  usename          | repl_user
  application_name | my_application
  client_addr      | 10.48.2.16
  client_hostname  | 
  client_port      | 40012
  backend_start    | 2024-03-10 19:58:07.914087+00
  backend_xmin     | 
  state            | streaming
  sent_lsn         | 0/3069FF8
  write_lsn        | 0/3069FF8
  flush_lsn        | 0/3069FF8
  replay_lsn       | 0/3069FF8
  write_lag        | 00:00:00.000237
  flush_lag        | 00:00:00.001506
  replay_lag       | 00:00:00.001541
  sync_priority    | 1
  sync_state       | sync
  reply_time       | 2024-03-11 22:16:33.619646+00
  ```

### Connecting to the Replica DB

- To connect to the database run the following command:

  ```
  kubectl run postgresql-pg-us1-client --rm --tty -i --restart='Never' --namespace database --image docker.io/bitnami/postgresql:16.2.0-debian-12-r6 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
    --command -- psql --host postgresql-pg-us1-read -U webapp_user -d webapp -p 5432
  ```

- Confirm the `todo` table is properly replicated

  ```
  webapp=> \dt
            List of relations
  Schema | Name | Type  |    Owner    
  --------+------+-------+-------------
  public | todo | table | webapp_user
  (1 row)

  webapp=> select * from todo;
  id | title  |           text           |          pub_date          
  ----+--------+--------------------------+----------------------------
    1 | Rocket | Build a rocket like Elon | 2024-03-11 17:44:49.182391
    2 | Gym    | Start weights            | 2024-03-11 18:00:15.24868
  (2 rows)

  webapp=> 
  ```

- To confirm streaming replication works on the replica:

  ```
  webapp=# select * from pg_stat_wal_receiver ;
  -[ RECORD 1 ]---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  pid                   | 257
  status                | streaming
  receive_start_lsn     | 0/3000000
  receive_start_tli     | 1
  written_lsn           | 0/3069FF8
  flushed_lsn           | 0/3069FF8
  received_tli          | 1
  last_msg_send_time    | 2024-03-11 22:18:33.660989+00
  last_msg_receipt_time | 2024-03-11 22:18:33.661047+00
  latest_end_lsn        | 0/3069FF8
  latest_end_time       | 2024-03-11 22:16:33.618147+00
  slot_name             | 
  sender_host           | postgresql-pg-us1-primary
  sender_port           | 5432
  conninfo              | user=repl_user password=******** channel_binding=prefer dbname=replication host=postgresql-pg-us1-primary port=5432 application_name=my_application fallback_application_name=walreceiver sslmode=prefer sslcompression=0 sslcertmode=allow sslsni=1 ssl_min_protocol_version=TLSv1.2 gssencmode=disable krbsrvname=postgres gssdelegation=0 target_session_attrs=any load_balance_hosts=disable
  ```

## Future work

Here are a list of things I could improve if given the time

- Expose a metric port for the flask app which can be used for scaling.
- Use GCP container registry for storing container images.
- Add a manual github job for releasing the application.
- Add a metric exporter for the Postgres cluster.
- And more!!!


Happy coding 😉
