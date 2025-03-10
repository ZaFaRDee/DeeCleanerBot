from pyrogram import Client, filters, enums

app = Client(
    "my_service_cleaner_bot",
    api_id="10118380",          # O'zingizning API ID
    api_hash="65fdab02294f44dee4dd452c0d1ce4e4",  # O'zingizning API HASH
    bot_token="8197677381:AAFk4vtzaPQO4t7ClCyqpr1UTRt-TLCXiKY" # BotFather bergan token
)

SERVICE_TYPES = [
    enums.MessageServiceType.NEW_CHAT_MEMBERS,
    enums.MessageServiceType.LEFT_CHAT_MEMBERS,
    enums.MessageServiceType.NEW_CHAT_PHOTO,
    enums.MessageServiceType.NEW_CHAT_TITLE,
    enums.MessageServiceType.VIDEO_CHAT_SCHEDULED,
    enums.MessageServiceType.VIDEO_CHAT_STARTED,
    enums.MessageServiceType.VIDEO_CHAT_ENDED,
    enums.MessageServiceType.DELETE_CHAT_PHOTO,
]

@app.on_message(filters.service)
async def delete_service_messages(client, message):
    if message.service in SERVICE_TYPES:
        try:
            await message.delete()
            print(f"✅ {message.service} xabari o'chirildi")
        except Exception as e:
            print(f"❌ Xatolik: {e}")

app.run()
