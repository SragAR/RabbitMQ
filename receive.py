import pika
#credentials = pika.PlainCredentials('guest', 'guest')
import cv2
import numpy as np
import pickle

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.4.6.33'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')
i = 1

def callback(ch, method, properties, body):
    global i
    obj = pickle.loads(body.decode('ASCII'))
    nparr = np.fromstring(obj['image'], np.uint8)
    print(obj['timestamp'])
    img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
    #cv2.imwrite('rec/'+str(i)+'.jpg', img)
    cv2.imshow('stream', img)
    c = cv2.waitKey(1)
    i += 1
    ch.basic_ack(delivery_tag=method.delivery_tag)

#only one task dispatched to a consumer at a time
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
