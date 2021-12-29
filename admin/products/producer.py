import os

import json
import pika
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = str(os.getenv('RABBIT_KEY'))
params = pika.URLParameters(SECRET_KEY)


class Producer:
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    def publish(self, method, body):
        properties = pika.BasicProperties(method)

        if not self.connection or self.connection.is_closed:
            self.connection = pika.BlockingConnection(params)
            self.channel = self.connection.channel()

        self.channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)


