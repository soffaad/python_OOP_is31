import asyncio
import random


async def worker(name, queue):
    while True:
        task = await queue.get()
        if task is None:
            break
        print(f"Worker {name}: начал задачу {task}")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"Worker {name}: завершил задачу {task}")
        queue.task_done()


async def main():
    task_queue = asyncio.Queue()
    workers = [asyncio.create_task(worker(f"W{i + 1}", task_queue)) for i in range(3)]

    for t in range(6):
        await task_queue.put(f"Задача-{t + 1}")
        await asyncio.sleep(0.2)

    for _ in workers:
        await task_queue.put(None)
    await asyncio.gather(*workers)


if __name__ == "__main__":
    asyncio.run(main())