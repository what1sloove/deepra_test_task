from typing import Optional

from pydantic import BaseModel


class MessageModel(BaseModel):
    name: str
    message: Optional[str] = None
