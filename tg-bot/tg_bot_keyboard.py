from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder


start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="да, нужно добавить учётку")],
        [KeyboardButton(text="нет, я передумала")],
    ],
    resize_keyboard=True,
)

restart_keyboard11 = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/start")]], resize_keyboard=True
)

delete_keyboard = ReplyKeyboardRemove()