from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def generate_random_number():
    random_number = random.randint(1000, 9999)
    return {"random_number": random_number}
