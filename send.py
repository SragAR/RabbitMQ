import pika
import os
import cv2
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
count = 1
for filename in os.listdir('images'):
	path = os.path.join('images', filename)
        obj = {}
	image = cv2.imread(path)
        if image is not None:
		obj['image'] = cv2.imencode('.jpg', image)[1].tostring()
		obj['timestamp'] = count
		channel.basic_publish(exchange='',
				      routing_key='task_queue',
				      body=pickle.dumps(obj))
		count += 1


connection.close()
