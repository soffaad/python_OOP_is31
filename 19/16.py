import asyncio

async def task_gather(name, delay):
    await asyncio.sleep(delay)
    return f"{name} завершена через {delay} сек"

async def main():
    results = await asyncio.gather(
        task_gather("A", 1),
        task_gather("B", 2),
        task_gather("C", 0.5)
    )
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())