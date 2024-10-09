from typing import Optional

from pydantic import BaseModel


class MessageModel(BaseModel):
    name: Optional[str] = "Recruto"
    message: Optional[str] = "Давай дружить"
