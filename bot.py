import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import anthropic
import asyncio

BOT_TOKEN = "твой_токен_от_botfather"
ANTHROPIC_KEY = "твой_ключ_от_anthropic"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я мини-AI, спрашивай про IT!")

@dp.message()
async def handle(message: types.Message):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        system="Ты IT-ассистент. Отвечай только на вопросы про программирование и технологии. Коротко, по делу, на русском.",
        messages=[{"role": "user", "content": message.text}]
    )
    await message.answer(response.content[0].text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
