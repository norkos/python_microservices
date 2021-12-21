import pika

params = pika.URLParameters('amqps://emeuxtkv:nO6QHNAsnc0ySVJYTkIEMLvtUsIB5-xi@roedeer.rmq.cloudamqp.com/emeuxtkv')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')


