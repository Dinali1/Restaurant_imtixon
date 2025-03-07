from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __


from bot.buttons.reply import main_control_button
from bot.dispatcher import dp
from bot.state import RestaurantSector

@dp.message(F.text == __("🥗 Salads"))
async def command_salads_handler(message: Message, state:FSMContext) -> None:
    text = [_("🥗 Cezar Salad"), _("🥗 Olivie Salad"), _("⬅️ Back (Main Menu)")]
    markup = main_control_button(text, (2, 1))
    await state.set_state(RestaurantSector.salad_menu)
    await message.answer(_("🥗 Welcome to Salads Menu"), reply_markup=markup)


@dp.message(F.text == __("🍕 Fastfood"))
async def command_salads_handler(message: Message, state:FSMContext) -> None:
    text = [_("🍔 Burger"), _("🌭 Hot-Dog"), _("⬅️ Back (Main Menu)")]
    markup = main_control_button(text, (2, 1))
    await state.set_state(RestaurantSector.fast_food_menu)
    await message.answer(_("🥗 Welcome to Salads Menu"), reply_markup=markup)


@dp.message(F.text == __("🥣 Hot Meals"))
async def command_salads_handler(message: Message, state:FSMContext) -> None:
    text = [_("🍚 Pilov"), _("🍜 Soup"), _("⬅️ Back (Main Menu)")]
    markup = main_control_button(text, (2, 1))
    await state.set_state(RestaurantSector.hot_meals_menu)
    await message.answer(_("🥗 Welcome to Salads Menu"), reply_markup=markup)