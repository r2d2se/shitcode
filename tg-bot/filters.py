from mailbox import Message
from typing import List

from aiogram.filters import BaseFilter 
from aiogram.types import message


class ByID(BaseFilter):
    def __init__(self, user_id: int | List[int]):
        self.user_id = user_id
    async def __call__ (self, message: Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id
        return message.from_user.id in self.user_id