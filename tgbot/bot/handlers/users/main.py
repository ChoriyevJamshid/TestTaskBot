from aiogram import types, F
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from django.utils import timezone

from tgbot.bot.keyboards import inline
from tgbot.bot.utils import google_sheet
from tgbot.bot.utils.payments import create_payment


async def start_handler(message: types.Message, state: FSMContext):
    payment_url, payment_id = create_payment(
        amount="2.00",
        chat_id=message.chat.id,
    )

    await message.answer(
        text="Hello world",
        reply_markup=await inline.inline_keyboard(payment_url)
    )


async def get_date_and_add_to_gs(message: types.Message, state: FSMContext):

    try:
        timezone.datetime.strptime(message.text, "%d.%m.%Y")
    except ValueError:
        return await message.answer(
            "Дата введена неверно"
        )
    await message.answer(
        "Дата введена верно"
    )
    await google_sheet.add_data_to_sheet_b(message.text)


async def callback_send_image(
        callback_query: types.CallbackQuery,
        callback_data: CallbackData,
        state: FSMContext
):
    await callback_query.message.answer_photo(
        photo="https://www.unite.ai/wp-content/uploads/2022/04/AI-Python-Libraries.png"
    )

    await callback_query.answer()


async def callback_google_sheet(
        callback_query: types.CallbackQuery,
        callback_data: CallbackData,
        state: FSMContext
):
    await callback_query.message.answer(
        text="Please wait ..."
    )

    value = await google_sheet.get_data_from_sheet_a2()
    await callback_query.message.answer(
        text=f"A2 value in Google Sheets: {value}"
    )
    await callback_query.answer()

