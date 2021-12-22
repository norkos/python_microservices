import pika
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()


from dotenv import load_dotenv
import os

from products.models import Product

load_dotenv()

SECRET_KEY = str(os.getenv('RABBIT_KEY'))
params = pika.URLParameters(SECRET_KEY)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    product_id = json.loads(body)
    product = Product.objects.get(id=product_id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started consuming')
channel.start_consuming()

channel.close()