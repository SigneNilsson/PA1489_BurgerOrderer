#Script for creating container with database

podman pull docker.io/library/mysql:latest;

$containerName = "menuStore";

$password = "bestgroupever";

#creating the database container with chosen name and password, running on port 5001.
podman run --name $containerName -e MYSQL_ROOT_PASSWORD=$password -d -p 3306:5001 mysql:latest;

