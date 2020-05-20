#!/bin/bash 

docker exec -w /code -it skosmg sh runDocker.sh
sleep 5
curl http://localhost:4000/graph_creation/data/config.ini
echo ""
echo "RESULTS IN $(pwd)/result/" 


