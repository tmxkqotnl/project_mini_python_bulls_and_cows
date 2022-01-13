#!/bin/bash

echo $1
cmd=$1

if [ $cmd = "up" ]
then
    docker-compose up -d
elif [ $cmd = "down" ]
then
    docker-compose down -v
elif [ $cmd = "reset" ]
then
    docker-compose down -v && docker-compose up -d
else
    echo "no matched key $cmd"
fi