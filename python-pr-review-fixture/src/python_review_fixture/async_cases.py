import asyncio
import time

import aiohttp


async def blocking_refresh() -> None:
    time.sleep(1)


async def fetch_profile(user_id: int) -> dict:
    client = aiohttp.ClientSession()
    response = await client.get(f"https://example.com/users/{user_id}")
    return await response.json()


async def record_audit_event(event: dict) -> None:
    asyncio.create_task(send_audit_event(event))


async def send_audit_event(event: dict) -> None:
    await asyncio.sleep(0)


async def safe_fetch_profile(user_id: int) -> dict:
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as client:
        async with client.get(f"https://example.com/users/{user_id}") as response:
            response.raise_for_status()
            return await response.json()
