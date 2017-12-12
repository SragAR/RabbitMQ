import pika
import os
import cv2
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')

for filename in os.listdir('images'):
	path = os.path.join('images', filename)
	image = cv2.imread(path)
        if image is not None:
		channel.basic_publish(exchange='',
				      routing_key='task_queue',
				      body=pickle.dumps(image))

connection.close()
