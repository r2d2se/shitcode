import os

from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database import database
from tg_bot_keyboard import (
    start_keyboard,
    restart_keyboard11,
    delete_keyboard,
    gender_keyboard
)

tg_bot = Router()


class Form(StatesGroup):
    FIO = State()
    date_born = State()
    number = State()
    job_title = State()
    departament = State()
    gender = State()
    rights = State()


@tg_bot.message(F.text.lower() == "старт")
@tg_bot.message(F.text.lower() == "рестарт")
@tg_bot.message(F.text.lower() == "restart")
@tg_bot.message(CommandStart())
async def start_message(message: types.Message):
    await message.answer(
        text="Добавить нового сотрудника?", reply_markup=start_keyboard
    )


@tg_bot.message(StateFilter("*"), F.text.lower() == "отмена")
@tg_bot.message(F.text.lower() == "нет, я передумала")
async def reboot_bot(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "Действия отменены, введите команду start", reply_markup=restart_keyboard11
    )


@tg_bot.message(
    StateFilter(None),
    F.text.lower() == "да, нужно добавить учётку",
)
async def add_uchetka(message: types.Message, state: FSMContext):
    await message.answer(
        "Введите ФИО, (Пример:Васильев Василий Васильевич)",
        reply_markup=delete_keyboard,
    )
    await state.set_state(Form.FIO)


@tg_bot.message(Form.FIO, F.text)
async def get_fio(message: types.Message, state: FSMContext):
    await state.update_data(fio=message.text)
    await message.answer("Введите дату рождения (Пример:10.10.1488)")
    await state.set_state(Form.date_born)


@tg_bot.message(Form.date_born, F.text)
async def get_date_born(message: types.Message, state: FSMContext):
    await state.update_data(date_born=message.text)
    await message.answer(
        "Введите номер телефона(Пример: 88005553535 или 8-800-555-35-35)"
    )
    await state.set_state(Form.number)


@tg_bot.message(Form.number, F.text)
async def get_number(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("Введите должность")
    await state.set_state(Form.job_title)


@tg_bot.message(Form.job_title, F.text)
async def get_job_title(message: types.Message, state: FSMContext):
    await state.update_data(job_title=message.text)
    await message.answer(
        "Укажите отдел (подразделение автоматически будет выбрано, как стажёры)"
    )
    await state.set_state(Form.departament)


@tg_bot.message(Form.departament, F.text.lower)
async def get_departament(message: types.Message, state: FSMContext):
    await state.update_data(departament=message.text)
    await message.answer("Введите пол (Пример: м или М, ж или Ж)",reply_markup=gender_keyboard)
    await state.set_state(Form.gender)


@tg_bot.message(Form.gender, F.text)
async def get_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await message.answer(
        "Права(Пример: Белявцев Дмитрий.Крайне важно указывать фамилию и имя, как указано в битриксе. Информация по правам тянется из него)"
    )
    await state.set_state(Form.rights)


@tg_bot.message(Form.rights, F.text)
async def get_rights(message: types.Message, state: FSMContext):
    await state.update_data(rights=message.text)
    data = await state.get_data()
    await database.sql_add_command(data)
    print(data)
    await message.answer(
        "Учётка пошла создаваться, ожидайте отправки данных уч.записи. Нужно ещё создать учётку?",
        reply_markup=start_keyboard,
    )
    os.system(
        "python F:\project\zaeblo\zaeblo\project.py"
    )  # тут указываем путь на серве
    await state.clear()
