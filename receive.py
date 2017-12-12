import pika
#credentials = pika.PlainCredentials('guest', 'guest')
import time
import cv2
import numpy as np
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')
i = 1

def callback(ch, method, properties, body):
    global i
    imge = pickle.loads(body.decode('ASCII'))
    cv2.imwrite('rec/'+str(i)+'.jpg', imge)
    i = i+1
    ch.basic_ack(delivery_tag=method.delivery_tag)
    if( i == 57):
    	connection.close()
#only one task dispatched to a consumer at a time
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
