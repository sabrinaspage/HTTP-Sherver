import asyncio

async def nested():
    return 42

async def main():
    # schedule nested() to run soon concurrently
    # with main()
    task = asyncio.create_task(nested())

    # task can be used to cancel nested() or simply be awaited to completion
    print(await task)

asyncio.run(main())