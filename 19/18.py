import asyncio

async def async_read(filename, delay):
    print(f"Чтение {filename} начато")
    await asyncio.sleep(delay)
    print(f"Чтение {filename} завершено")
    return f"Данные из {filename}"

async def main():
    files = [("file1.txt", 1), ("file2.txt", 2), ("file3.txt", 0.5)]
    tasks = [async_read(f, d) for f, d in files]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())