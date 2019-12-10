# A Simple Flask Python Application with a MySQL database

## Before Running
The `server.py` contains the flask application with a default endpoint which will
connect to the MySQL database through the docker host ip.

To get the docker host ip run:
`docker inspect {NETWORK_ID} | grep Gateway`

The `NETWORK_ID` can be found by running:
`docker network ls`

A JSON response will be returned when you navigate to localhost:5000.

## Run Configuration
To run the application you just need to navigate to the directory with the
docker-compose.yml file in your terminal/console.

To run the application:
`docker-compose up`

If you make any modifications to the `server.py` file you may need to run with
the following argument to rebuild the docker image:
`docker-compose up --build`

The server is running on python version 3.6.

