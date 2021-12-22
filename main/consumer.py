import pika

params = pika.URLParameters('amqps://emeuxtkv:nO6QHNAsnc0ySVJYTkIEMLvtUsIB5-xi@roedeer.rmq.cloudamqp.com/emeuxtkv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started consuming')
channel.start_consuming()

channel.close()