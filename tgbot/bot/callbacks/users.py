from aiogram.filters.callback_data import CallbackData


class SendIMageCallbackData(CallbackData, prefix="image"):
    pass


class GSCallbackData(CallbackData, prefix="gs_value"):
    pass


class PaymentCallbackData(CallbackData, prefix="payment"):
    pass
