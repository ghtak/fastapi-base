import asyncio


def run_test(func):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(func())
