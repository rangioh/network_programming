import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def stop_after(loop, when):
    await asyncio.sleep(when)
    print(what)

loop = asyncio.get_event_loop()
loop.create_task(say('first'))
