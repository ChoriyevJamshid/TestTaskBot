from typing import Tuple
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardButton


async def inline_keyboard(payment_url: str, sizes: Tuple[int] = (2,)) -> InlineKeyboardMarkup:
    payment_params = {
        "id": "po-285ec15d-0003-5000-a000-08d1bec7dade",
        "amount": {
            "value": "2.00",
            "currency": "RUB"
        },
        "status": "succeeded",
        "payout_destination": {
            "type": "yoo_money",
            "account_number": "4100116075156746"
        },
        "description": "Выплата по заказу № 37",
        "created_at": "21.06.2021T14:28:45.132Z",
        "metadata": {
            "order_id": "37"
        },
        "test": "test"
    }

    builder = InlineKeyboardBuilder()
    btn_yandex_link = InlineKeyboardButton(
        text="Yandex map",
        url="https://yandex.uz/maps/44/izhevsk/house/ulitsa_lenina_1/YUoYdw5oTUEAQFtsfXR1cnpjbQ==/?ll=53.198446%2C56.843609&z=17"
    )
    btn_payment = InlineKeyboardButton(
        text="Payment 2 RUB",
        url=payment_url
    )
    btn_image = InlineKeyboardButton(
        text="Image",
        callback_data="image"
    )
    btn_google_sheet = InlineKeyboardButton(
        text="Get value from gs",
        callback_data="gs_value"
    )
    builder.add(
        btn_yandex_link,
        btn_payment,
        btn_image,
        btn_google_sheet
    )
    return builder.adjust(*sizes).as_markup()
