import asyncio
import random

async def producer(queue, n):
    for i in range(n):
        await asyncio.sleep(random.uniform(0.2, 0.5))
        await queue.put(f"data-{i}")
        print(f"Producer: добавил data-{i}")
    await queue.put(None)

async def consumer(queue, name):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumer {name}: обработал {item}")
        await asyncio.sleep(random.uniform(0.3, 0.7))
        queue.task_done()

async def main():
    q = asyncio.Queue()
    prod = asyncio.create_task(producer(q, 5))
    cons1 = asyncio.create_task(consumer(q, "A"))
    cons2 = asyncio.create_task(consumer(q, "B"))
    await prod
    await q.join()
    await cons1
    await cons2

if __name__ == "__main__":
    asyncio.run(main())