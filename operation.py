import aiohttp


API_URL = "http://octopus-app-3gdu5.ondigitalocean.app"


async def send_signal(game: str, signal: str, signal_type: str):
    async with aiohttp.ClientSession() as session:
        data = {"game": game, "message": signal, "type": signal_type}
        await session.post(f"{API_URL}/signal", json=data)
        print(game, "signal sent")
