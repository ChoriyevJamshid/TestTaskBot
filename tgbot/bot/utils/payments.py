import uuid
from yookassa import Payment, Configuration
from django.conf import settings


def create_payment(amount, chat_id):

    Configuration.account_id = settings.YOOKASSA_ACCOUNT_ID
    Configuration.secret_key = settings.YOOKASSA_SECRET_KEY
    Configuration.api_url = "https://api.yookassa.ru/v3"

    print(f"{Configuration.account_id = }")
    print(f"{Configuration.secret_key = }")

    id_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/JmTestBot_bot"
        },
        "capture": True,
        "save_payment_method": True,
        "description": "Оплата заказа ...",
        "metadata": {
            "chat_id": chat_id
        }
    }, id_key)

    return payment.confirmation.confirmation_url, payment.id
