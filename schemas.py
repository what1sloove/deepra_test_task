from typing import Optional

from pydantic import BaseModel


class MessageModel(BaseModel):
    name: Optional[str] = "test_name"
    message: Optional[str] = "test_message"
