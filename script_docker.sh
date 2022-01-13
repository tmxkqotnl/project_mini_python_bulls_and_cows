#!/bin/sh

echo $1

cmd=$1

if [${cmd} -eq "up"]; 
then
    docker-compose up -d
elif [${cmd} -eq "down"];
then
    docker-compose down -v
elif [${cmd} -eq "reset"]
    docker-compose down -v && docker-compose up -d
