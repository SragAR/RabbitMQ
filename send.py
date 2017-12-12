import pika
import os
import cv2
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

for filename in os.listdir('images'):
	path = os.path.join('images', filename)
	image = cv2.imread(path)
        if image is not None:
		image = cv2.imencode('.jpg', image)[1].tostring()
		print('sending', type(image))
		channel.basic_publish(exchange='',
				      routing_key='task_queue',
				      body=image)

print(" [x] Sent 'Hello World!'")
connection.close()
