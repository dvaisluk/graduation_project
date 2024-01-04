from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import button_case_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command


async def make_changes_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать, Администратор', reply_markup=button_case_admin)



async def update_reserve_handler(message: types.Message):
    args = message.text.split()[1:]
    
    if len(args) != 3:
        await message.reply("Используйте команду в формате: /update_reserve <coin> <amount> <amount_in_rub>")
        return
    
    coin, amount, amount_in_rub = args
    
    try:
        amount = float(amount)
        amount_in_rub = float(amount_in_rub)
    except ValueError:
        await message.reply("amount и amount_in_rub должны быть числами.")
        return
    
    success = await sqlite_db.update_reserve(coin, amount, amount_in_rub)
    
    if success:
        await message.reply(f"Значения для {coin} успешно обновлены.")
    else:
        await message.reply("Ошибка при обновлении значений.")




def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['admin'])
    dp.register_message_handler(update_reserve_handler, Command("update_reserve", prefixes='/'))


