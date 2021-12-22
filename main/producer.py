import os

import json
import pika
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = str(os.getenv('RABBIT_KEY'))
params = pika.URLParameters(SECRET_KEY)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)


