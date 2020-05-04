docker exec -w /code -it skosmg bash runDocker.sh
sleep 5
curl http://localhost:4000/graph_creation/data/config.ini
sleep 5
echo "\n RESULTS IN $(pwd)/result/"
