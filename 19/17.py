import asyncio
import random

async def delayed_task(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} завершена (задержка {delay:.2f} сек)")

async def main():
    tasks = [asyncio.create_task(delayed_task(f"Задача-{i}", random.uniform(0.5, 3))) for i in range(5)]
    for t in tasks:
        await t

if __name__ == "__main__":
    asyncio.run(main())