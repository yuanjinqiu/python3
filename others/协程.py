import asyncio

async \
    def foo1():
    print('hello')
    await asyncio.sleep(2)
    print('world')

async \
    def foo2():
    print('jin')
    await asyncio.sleep(2)
    print('qiu')

task = [
    asyncio.ensure_future(foo1()),
    asyncio.ensure_future(foo2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
