
import pyperclip
import asyncio
from telegram import Bot


TOKEN = '7423032401:AAHP3yAaGLSLCnXIY-uINVvG-tpog0ZGnoU'

CHAT_ID = '603004587'

async def send_message_with_clickable_link(bot, chat_id, phone_number):

    text = f'Phone Number: <a href="tel:{phone_number}">+91{phone_number}</a>'

    await bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')

async def monitor_clipboard():
    last_clipboard_content = ""
    bot = Bot(token=TOKEN)

    while True:
        clipboard_content = pyperclip.paste()
        if clipboard_content != last_clipboard_content:
            last_clipboard_content = clipboard_content
            print(f"New clipboard content detected: {clipboard_content}")


            if clipboard_content.isdigit() and len(clipboard_content) >= 10 and len(clipboard_content) <= 15:
                await send_message_with_clickable_link(bot, CHAT_ID, clipboard_content)
        await asyncio.sleep(1)

def main():
    asyncio.run(monitor_clipboard())

if __name__ == "__main__":
    main()


