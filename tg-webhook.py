from config import API_TOKEN
import logging
from aiogram import Bot, Dispatcher, types
import handlers

import json

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(handlers.router)


async def process_event(event):
    update = types.Update.model_validate(json.loads(event['body']), context={"bot": bot})
    await dp.feed_update(bot, update)


async def webhook(event, context):
    if event['httpMethod'] == 'POST':
        # Bot and dispatcher initialization
        # Объект бота

        await process_event(event)
        return {'statusCode': 200, 'body': 'ok'}

    return {'statusCode': 405}
