docker rm -f $(docker ps -qa)
sleep 5
docker rmi skos-generation_skosmg:latest
sleep 5
docker-compose up -d
sleep 5
docker exec -w /code -it skosmg bash runDocker.sh
sleep 5
curl http://localhost:4000/graph_creation/data/config.ini
sleep 5
echo "FINISH"
