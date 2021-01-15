import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():

    task1 = asyncio.create_task(say_after(2, 'dee'))
    task2 = asyncio.create_task(say_after(1, 'doo'))

    print(f"started at {time.strftime('%X')}")

    # wait until both tasks are completed (2 seconds)
    await task1
    await task2

    print(f"ended at {time.strftime('%X')}")

asyncio.run(main())

# because asyncio.create_tasks means the tasks run at the same tim as each other
# doo shall print first, then dee

# w/o create_task, it would simply be dee, then doo