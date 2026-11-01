# Posts the media file (ad.mp4 or flyer.jpg) with ad.txt as caption from the Telegram account in TG_SESSION.
import os, asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

MEDIA = os.environ.get("MEDIA", "ad.mp4")

async def main():
    client = TelegramClient(StringSession(os.environ["TG_SESSION"]),
                            int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"])
    await client.start()
    caption = open("ad.txt", encoding="utf-8").read().strip()
    for chat in os.environ["CHAT_ID"].split():
        target = int(chat) if chat.lstrip("-").isdigit() else chat
        try:
            await client.send_file(target, MEDIA, caption=caption, supports_streaming=True)
            print("Posted to", chat)
        except Exception as e:
            print("Failed for", chat, e)
        await asyncio.sleep(30)
    await client.disconnect()

asyncio.run(main())
