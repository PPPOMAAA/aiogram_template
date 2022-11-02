from aiogram import types, Dispatcher


async def user_start(message: types.Message):
    await message.reply("Hello, user!")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=['start'], is_admin=None)
