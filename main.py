from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root(name: Optional[str] = "Recruto", message: Optional[str] = "Давай дружить"):
    return {f"Hello {name}! {message}"}
