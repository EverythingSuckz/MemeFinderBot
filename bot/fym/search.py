from typing import Optional

import aiohttp

from bot import fym

async def get_memes(query: str = "", offset: int = 0) -> Optional[fym.Result]:
    async with aiohttp.ClientSession(headers = {'Content-Type': 'application/json'}) as client:
        async with client.post(f"{fym.BASE_URL}/api/v1/search", data= '{"search": "%s", "offset": %s}' % (query or "", offset or 0)) as resp:
            if resp.status == 200:
                data =  await resp.json()
                return [fym.Result.from_json(d) for d in data]
            else:
                print(resp)
                return None