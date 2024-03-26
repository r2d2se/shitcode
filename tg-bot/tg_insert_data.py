from aiogram import F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from tg_bot_keyboard import start_keyboard, restart_keyboard11
tg_bot = Router()


class Form(StatesGroup):
    start = State()
    FIO = State()

@tg_bot.message(StateFilter(None), CommandStart())
async def start_message(message: types.Message, state: FSMContext):
    await message.answer(
        text="Добавить нового сотрудника?", reply_markup=start_keyboard
    )
    await state.set_state(Form.start)


@tg_bot.message(StateFilter("*"), F.text.lower() == "отмена")
@tg_bot.message(F.text.lower() == 'нет, я передумала')
async def reboot_bot(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(
        "Действия отменены, введите команду start", reply_markup=restart_keyboard11
    )


@tg_bot.message(Form.start, F.text.lower() == "да, нужно добавить учётку", )
async def add_uchetka(message: types.Message, state: FSMContext):
    await state.update_data()
    await message.answer("Введите ФИО, (Васильев Василий Васильевич)")
    await state.set_state(Form.FIO)

@tg_bot.message(Form.FIO, F.text.lower() == "да, нужно добавить учётку")