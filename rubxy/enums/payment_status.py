from enum import auto
from .auto_name import AutoName

class PaymentStatus(AutoName):
    PAID = auto()
    "Payment paid"

    NOT_PAID = auto()
    "Payment not paid"