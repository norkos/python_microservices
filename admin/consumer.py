import pika

from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = str(os.getenv('RABBIT_KEY'))
params = pika.URLParameters(SECRET_KEY)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started consuming')
channel.start_consuming()

channel.close()