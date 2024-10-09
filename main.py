from fastapi import FastAPI

from schemas import MessageModel

app = FastAPI()


@app.get("/")
def read_root(data: MessageModel):
    return f"Hello {data.name}! {data.message}"
