import pika
#credentials = pika.PlainCredentials('guest', 'guest')
import time
import cv2
import numpy as np

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')
i = 1

def callback(ch, method, properties, body):
    global i
    time.sleep(1)
    nparr = np.fromstring(body, np.uint8)
    imge = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
    print("Received", imge)  
    cv2.imwrite('rec/'+str(i)+'.jpg', imge)
    i = i+1
    ch.basic_ack(delivery_tag=method.delivery_tag)

#only one task dispatched to a consumer at a time
channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
                      queue='task_queue')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
