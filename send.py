import pika
import cv2
import pickle
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')


cap = cv2.VideoCapture(0)

while cap.isOpened():
	_,image = cap.read()
	if _ == 0:
    		break
        if image is not None:
                obj = {}
		obj['image'] = cv2.imencode('.jpg', image)[1].tostring()
		obj['timestamp'] = time.time()
		channel.basic_publish(exchange='',
				      routing_key='task_queue',
				      body=pickle.dumps(obj))


connection.close()
