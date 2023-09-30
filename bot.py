import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import Command
from environs import Env

import crud
from auth import decodeJWT
from config import settings

env = Env()
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hi, plz, send me ur token.")


@router.message()
async def message_handler(msg: Message):
    payload: dict = decodeJWT(msg.text)
    if crud.add_chat_to_user(payload.get('userID'), msg.chat.id):
        await msg.answer("U are registered.")
    else:
        await msg.answer("U are NOT registered.")


async def main():
    bot: Bot = Bot(token=settings.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())