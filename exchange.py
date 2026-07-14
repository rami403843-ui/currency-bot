import aiohttp

URL = "https://www.cbr-xml-daily.ru/daily_json.js"

async def get_currency():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            data = await response.json(content_type=None)
            return data
