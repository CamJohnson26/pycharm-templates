import sys

import pika
from dotenv import load_dotenv
import os

load_dotenv()
token = os.environ.get("api-token")

RABBITMQ_URL = os.getenv("RABBITMQ_URL")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))
RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")

MY_QUEUE_NAME = 'my_queue'


def my_queue_callback(ch, method, properties, body):
    """Callback function for the queue

    This function will be called when a message is received from the queue."""
    print(" [x] Received %r" % body)


def setup_rabbitmq(queues: tuple[str, callable]):
    """Setup RabbitMQ connection and channel"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_URL, port=RABBITMQ_PORT,
                                                                   credentials=pika.PlainCredentials(RABBITMQ_USERNAME,
                                                                                                     RABBITMQ_PASSWORD)))
    channel = connection.channel()

    for queue in queues:
        channel.queue_declare(queue=queue[0])
        channel.basic_consume(queue=queue[0], on_message_callback=queue[1], auto_ack=True)

    return channel


if __name__ == "__main__":
    """Main function to run the script

    This function will run the script and setup the RabbitMQ connection and channel."""
    try:
        queue_names = [(MY_QUEUE_NAME, my_queue_callback)]
        setup_rabbitmq(queue_names)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
