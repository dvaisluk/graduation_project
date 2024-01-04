from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('🤖 Отбор ChatGpt')
b2 = KeyboardButton('Ⓜ️ Пройти тест')
b3 = KeyboardButton('📝 Поддержка')
b4 = KeyboardButton('💼 Профиль')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2).row(b3, b4)
