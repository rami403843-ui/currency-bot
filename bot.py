import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from exchange import get_currency
from states import CurrencyState

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("rates"))
async def cmd_rates(message: Message, state: FSMContext):
    await message.answer("Введите трехзначный код валюты (например, USD, EUR, KGS):")
    await state.set_state(CurrencyState.waiting_for_code)

@dp.message(CurrencyState.waiting_for_code)
async def process_code(message: Message, state: FSMContext):
    code = message.text.upper()
    data = await get_currency()
    if code in data["Valute"]:
        currency = data["Valute"][code]
        name = currency["Name"]
        value = currency["Value"]
        previous = currency["Previous"]
        await message.answer(
            f"Валюта: {name} ({code})\n"
            f"Текущий курс: {value} руб.\n"
            f"Предыдущий курс: {previous} руб."
        )
        await state.clear()
    else:
        await message.answer("Валюта не найдена, попробуйте еще раз.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
