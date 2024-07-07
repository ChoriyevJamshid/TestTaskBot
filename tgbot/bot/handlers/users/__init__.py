from aiogram import Router, F
from aiogram.filters import CommandStart

from tgbot.bot.callbacks.users import *

from .main import *


def prepare_router() -> Router:
    router = Router()
    router.message.filter(F.chat.type == "private")

    # Registering the message handlers
    router.message.register(start_handler, CommandStart())
    router.message.register(get_date_and_add_to_gs)

    # Registering the callback handlers
    router.callback_query.register(callback_send_image, SendIMageCallbackData.filter())
    router.callback_query.register(callback_google_sheet, GSCallbackData.filter())
    return router
