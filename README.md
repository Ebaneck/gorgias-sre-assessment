# gorgias-sre-assessment
A simple flask application deployed on GKE

## Docker instructions

To create a docker image execute: 

`docker build . -t flaskapp`

To run the docker image execute:

`docker run -p 5000:5000 flaskapp` and visit with your browser http://localhost:5000
