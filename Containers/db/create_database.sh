#!/bin/bash

# If the database container called menuStore exists, stop and remove it
podman stop menuStore
podman rm menuStore

# Pull the latest MySQL image
podman pull docker.io/library/mysql:latest

# Creating the variables needed to make the container
containerName="menuStore"
password="bestgroupever"

# Creating the MySQL database container with chosen name and password, running on port 5006
podman run --name $containerName -e MYSQL_ROOT_PASSWORD=$password -d -p 5006:3306 mysql:latest

# Wait for the MySQL server to initialize (add a sleep to ensure MySQL is ready)
sleep 20  # Adjust the time if necessary, depending on how long the container takes to initialize

# Copy the SQL script to the container
podman cp ./menuStore.sql $containerName:/tmp/

# Run the SQL script inside the container
podman exec -it $containerName mysql -u root -p$password -e "source /tmp/menuStore.sql"