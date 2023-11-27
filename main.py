from room import handle_signal

from constants import group_usernames

from telethon.sync import TelegramClient
from telethon import events

api_id = 11325875
api_hash = '38280a3a5ad3bdca9cfa078708e686b7'

client = TelegramClient('session', api_id, api_hash)


async def get_entities(usernames: list) -> list:
    return [await client.get_entity(username) for username in usernames]


async def main():
    await client.start(lambda: "+5561995222034", lambda: "15Ago1945.")

    entities = await get_entities(group_usernames)

    @client.on(events.NewMessage(chats=entities))
    async def handle_message(event):
        await handle_signal(event)

    await client.run_until_disconnected()


if __name__ == '__main__':
    client.loop.run_until_complete(main())
