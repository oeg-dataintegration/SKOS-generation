#!/bin/bash 
python3 main.py
yarrrml-parser -i mapping.yaml -o mapping.ttl
path=$(pwd)
docker rm -f rdfizerContainer
sleep 5
docker run --name rdfizerContainer -d -p 4000:4000 -v ${path}:/data rdfizer
sleep 5
curl http://localhost:4000/graph_creation/data/config.ini
