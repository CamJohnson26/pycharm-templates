"""This module contains the queue name and callback function
"""

import aio_pika
MY_QUEUE_NAME = 'my_queue'


async def my_queue_callback(message: aio_pika.IncomingMessage):
    """Callback function for the queue

    This function will be called when a message is received from the queue."""
    try:
        print(f" [x] Received {message.body.decode()}")
        await message.ack()
    except Exception as e:
        print("Error:", e)
        await message.reject(requeue=False)


def get_my_queue() -> tuple[str, callable]:
    """Get the queue name and callback function

    This function will return the queue name and callback function."""
    return MY_QUEUE_NAME, my_queue_callback
