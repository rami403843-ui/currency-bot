from aiogram.fsm.state import State, StatesGroup

class CurrencyState(StatesGroup):
    waiting_for_code = State()
