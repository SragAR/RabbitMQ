import pika
#credentials = pika.PlainCredentials('guest', 'guest')
#parameters = pika.ConnectionParameters('localhost', 30001, '/', credentials, socket_timeout=2)
#pika.BlockingConnection(parameters)
#connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
