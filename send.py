import pika
#credentials = pika.PlainCredentials('guest', 'guest')
#parameters = pika.ConnectionParameters('localhost', 30001, '/', credentials, socket_timeout=2)
#pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body='Hello World!',
		      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
