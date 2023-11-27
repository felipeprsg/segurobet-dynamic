import aiohttp


API_URL = "http://localhost:3001"


async def send_signal(game: str, signal: str, signal_type: str):
    async with aiohttp.ClientSession() as session:
        data = {"game": game, "message": signal, "type": signal_type}
        await session.post(f"{API_URL}/signal", json=data)
        print(game, "signal sent")
