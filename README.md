#Run RabbitMQ server
docker run -d --hostname rabbit1 --name rabbit1 -e RABBITMQ_ERLANG_COOKIE=rabbitcluster -p 5672:5672 -p 15672:15672 rabbitmq:management

#List the queues

docker exec rabbit1 rabbitmqctl list_queues
