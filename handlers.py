from aiogram import types, F, Router
from aiogram.filters.command import Command
from services import get_currency

router = Router()


# Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добрый день. Как вас зовут?")


@router.message(F.text != '/start')
async def cmd_start(message: types.Message):
    user_name = message.text
    usd = await get_currency()
    if usd > 0:
        await message.answer(f"Рад знакомству, {message.text}! Курс доллара сегодня {usd}р")
    else:
        await message.answer(f"Рад знакомству, {message.text}! Сервис по курсу валют недоступен")
