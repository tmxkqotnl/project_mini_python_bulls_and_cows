#!/bin/sh

val=$1
echo ${val}

conda install psycopg2 -n ${val}