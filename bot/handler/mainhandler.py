from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __
from sqlalchemy import select, insert
from sqlalchemy.orm import sessionmaker

from bot.buttons.reply import main_control_button
from bot.dispatcher import dp
from bot.state import RestaurantSector
from db.config import User, engine

session = sessionmaker(engine)()

@dp.message(RestaurantSector.languages_menu, F.text == __("⬅️ Back (Main Menu)") )
@dp.message(RestaurantSector.restaurant_menu, F.text == __("⬅️ Back (Main Menu)") )
@dp.message(RestaurantSector.phone_menu, F.text == __("⬅️ Back (Main Menu)") )

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    if isinstance(message, CallbackQuery):
        pass
    else:
        query = select(User).filter(User.user_id == message.chat.id)
        user = session.execute(query).scalar()
        if not user:
            user = {
                "user_id": message.chat.id,
                "username": message.from_user.username
            }
            query = insert(User).values(**user)
            session.execute(query)
            session.commit()
    texts = [_("🍽 Restaurant Menu"), _("📞 Connect with us"), _("🇺🇿🇬🇧 Languages")]
    markup = main_control_button(texts, (2, 1))
    await message.answer(_("🏠 Main Menu"), reply_markup=markup)

@dp.message(F.text == __("🇺🇿🇬🇧 Languages"))
async def products_menu_handler(message: Message, state:FSMContext) -> None:
    texts = [_("🇺🇿 Uzbek"), _("🇬🇧 English"), _("⬅️ Back (Back to main menu)")]
    markup = main_control_button(texts, (2,1))
    await state.set_state(RestaurantSector.languages_menu)
    await message.answer(_("Choose Language"), reply_markup=markup)

@dp.message(RestaurantSector.languages_menu)
async def languages_menu_handler(message: Message, state:FSMContext, i18n) -> None:
    map_lang = {
        "🇺🇿 Uzbek" : 'uz',
        "🇬🇧 English" : 'en'
    }
    await state.clear()
    code = map_lang.get(message.text)
    await state.update_data({"locale": code})
    i18n.current_locale = code
    texts = [_("🍽 Restaurant Menu") , _("📞 Connect with us"), _("🇺🇿🇬🇧 Languages")]
    markup = main_control_button(texts, (2, 1))
    await message.answer(_("🏠 Main menu"), reply_markup=markup)


@dp.message(RestaurantSector.hot_meals_menu, F.text == __("⬅️ Back (Main Menu)") )
@dp.message(RestaurantSector.fast_food_menu, F.text == __("⬅️ Back (Main Menu)") )
@dp.message(RestaurantSector.salad_menu, F.text == __("⬅️ Back (Main Menu)") )
@dp.message(F.text == __("🍽 Restaurant Menu"))
async def command_menu_handler(message: Message, state:FSMContext) -> None:
    texts = [_("🥗 Salads"), _("🍕 Fastfood"), _("🥣 Hot Meals"), _("⬅️ Back (Main Menu)")]
    markup = main_control_button(texts, (3, 1))
    await state.set_state(RestaurantSector.restaurant_menu)
    await message.answer("🍽 Welcome to Restaurant Menu", reply_markup=markup)

@dp.message(F.text == __("📞 Connect with us"))
async def command_connect_handler(message: Message, state:FSMContext) -> None:
    texts = [_("📞 +998936160099"), _("⬅️ Back (Main Menu)")]
    markup = main_control_button(texts, (2,))
    await state.set_state(RestaurantSector.phone_menu)
    await message.answer(_("If you have problem call shown number"), reply_markup=markup)