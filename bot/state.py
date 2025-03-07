from aiogram.fsm.state import StatesGroup, State


class RestaurantSector(StatesGroup):
    restaurant_menu = State()
    salad_menu = State()
    phone_menu = State()
    fast_food_menu = State()
    hot_meals_menu = State()
    languages_menu = State()