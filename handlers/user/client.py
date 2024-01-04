from aiogram import types, Dispatcher
from keyboards import kb_client
from aiogram.dispatcher import FSMContext
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text
from create_bot import bot


async def cmd_start(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username
    if username is None:
        username = message.from_user.first_name
    user_exists = sqlite_db.registration_check(telegram_id)
    if not user_exists:
        try:
            referrer_id = message.get_args()
            sqlite_db.register_user(telegram_id, username, referrer_id)
        except ValueError:
            sqlite_db.register_user(telegram_id, username, 0)
        await message.reply(f"Привет, {message.from_user.first_name}! Вы успешно зарегистрированы.", reply_markup=kb_client)

    else:
        await message.reply("Вы уже зарегистрированы.", reply_markup=kb_client)



async def view_profile(message: types.Message, state: FSMContext):
    await state.finish()

    username = message.from_user.username
    if username is None:
        username = message.from_user.first_name

    await message.answer(f"""<b>💼 Личный кабинет:

📎 ID: {message.from_user.id}
📌️ Username: @{username}
💼 Профессия: 

👥 Реферальная система:
🔗 Ссылка: https://t.me/FindEduBot?start={message.from_user.id}
👦 Количество рефералов: {sqlite_db.count_referrals(message.from_user.id)}</b>""", parse_mode="HTML")


async def view_support(message: types.Message, state: FSMContext):
    await message.answer(
        """<b>🧑‍🔧Возникли проблемы или нашли баг? Напишите в нашу службу поддержки ;)</b>""", parse_mode="HTML"
    )


async def echo(message: types.Message):
    await message.answer('<b>❌ Что-то пошло не так, повторите действие заново!</b>', parse_mode='HTML', reply_markup=kb_client)




def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(view_profile, Text('💼 Профиль'), state='*')
    dp.register_message_handler(view_support, Text('👨‍💻 Поддержка'), state='*')
    dp.register_message_handler(echo, lambda message: message.text.lower()[
                                0] != '/', content_types=types.ContentTypes.TEXT)
