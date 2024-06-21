DOCKER_COMPOSE_FILE="docker-compose.yml"

echo "Setting up the postgres DB..."
docker-compose -f $DOCKER_COMPOSE_FILE up -d
sleep 5
echo "Running the ETL pipeline..."
python -m main
echo "ETL run finished, verifying..."
NUMBER_OF_ROWS=$(PGPASSWORD="test_user" psql -h localhost -U test_user -p 5000 -d lottery -t -A -c "SELECT COUNT(*) FROM winning_numbers")
echo $NUMBER_OF_ROWS
if [ $NUMBER_OF_ROWS -ge 1643 ]; then
    echo "The ETL run was successful!"
else
    echo "The ETL run failed!"
fi
docker-compose -f $DOCKER_COMPOSE_FILE down