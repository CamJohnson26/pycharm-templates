import pika
from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")


def publish_message(message: str, queue_name: str):
    """Publish a message to the queue

    This function will publish a message to the queue."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_URL, port=RABBITMQ_PORT,
                                                                   credentials=pika.PlainCredentials(RABBITMQ_USERNAME,
                                                                                                     RABBITMQ_PASSWORD)))
    channel = connection.channel()
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)
    connection.close()
