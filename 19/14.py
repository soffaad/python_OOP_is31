import asyncio

async def simple_async():
    print("Начало асинхронной функции")
    await asyncio.sleep(1)
    print("После задержки")

if __name__ == "__main__":
    asyncio.run(simple_async())