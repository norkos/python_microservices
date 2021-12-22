import pika, json

params = pika.URLParameters('amqps://emeuxtkv:nO6QHNAsnc0ySVJYTkIEMLvtUsIB5-xi@roedeer.rmq.cloudamqp.com/emeuxtkv')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)


