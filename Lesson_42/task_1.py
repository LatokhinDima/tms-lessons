import time
import asyncio
import random

async def wait_random_time():
    n = random.randint(1, 10)
    print(f"Начало ожидания {n} секунд")
    await asyncio.sleep(n)
    print(f"Конец работы {n} секунд")

async def main():
    tasks = [asyncio.create_task(wait_random_time()) for _ in range(100)]
    await asyncio.gather(*tasks)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f'Total time: {end_time - start_time} seconds')
