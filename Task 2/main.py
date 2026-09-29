from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the Math API!"}


@app.get("/multiply/{number}")
def multiply(number: int):
    return {
        "number": number,
        "result": number * 5
    }


@app.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "result": number * number
    }