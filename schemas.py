from typing import Optional

from pydantic import BaseModel


class MessageModel(BaseModel):
    name: Optional[str] = None
    message: Optional[str] = None
