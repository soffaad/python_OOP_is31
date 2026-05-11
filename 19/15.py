import asyncio

async def async_task(name, delay):
    await asyncio.sleep(delay)
    print(f"Задача {name} завершена")

async def main():
    await asyncio.gather(
        async_task("A", 1),
        async_task("B", 0.5),
        async_task("C", 1.5)
    )

if __name__ == "__main__":
    asyncio.run(main())