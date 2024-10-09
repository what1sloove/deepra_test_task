from fastapi import FastAPI, Depends

from schemas import MessageModel

app = FastAPI()


@app.get("/")
def read_root(data: MessageModel = Depends()):
    return f"Hello {data.name}! {data.message}"
