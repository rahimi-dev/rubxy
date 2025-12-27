import rubxy

from rubxy import enums
from typing import Optional

from .object import Object

class PaymentStatus(Object):
    def __init__(
        self,
        *,
        client: "rubxy.Client" = None,
        payment_id: Optional[str] = None,
        status: Optional["enums.PaymentStatus"] = None
    ):
        super().__init__(client=client)

        self.payment_id = payment_id
        self.status = status