from typing import List, Optional
from rubxy import types

class Keypad:
    def __init__(
        self,
        rows: List[List["types.Button"]],
        resize_keyboard: Optional[bool] = None,
        on_time_keyboard: Optional[bool] = None
    ):
        self.rows = rows
        self.resize_keyboard = resize_keyboard
        self.on_time_keyboard = on_time_keyboard
    
    def _to_dict(self):
        return dict(
            rows=[
                dict(
                    buttons=[
                        button._to_dict() for button in row
                    ]
                ) for row in self.rows
            ],
            resize_keyboard=self.resize_keyboard,
            on_time_keyboard=self.on_time_keyboard
        )
    