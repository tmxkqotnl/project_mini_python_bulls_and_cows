#!/bin/bash

val=$1
echo ${val}

conda install psycopg2 -n ${val}
pip install python-dotenv -n ${val}