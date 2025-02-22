# Question: Day 54: Write async function to fetch multiple URLs concurrently.
import aiohttp
import asyncio

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://python.org',
        'https://google.com',
        'https://github.com'
    ]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(f"Fetched {len(results)} pages")

asyncio.run(main())
