import asyncio


SLEEP_TIME = 1


async def background_task():
    """ Example of a background task. """
    while True:
        print("Tick")
        await asyncio.sleep(SLEEP_TIME)


if __name__ == '__main__':
    """ Run the background task.
    The background task will run forever, until the program is killed.
    """
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(background_task())
        loop.run_forever()
        loop.close()
    except Exception as e:
        print("Error:", e)
        loop.close()
