from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

books = []


# Book data
class Book(BaseModel):
    title: str
    author: str


# Add book
@app.post("/addbook")
def add_book(book: Book):
    books.append(book)

    return {
        "message": "Book added successfully",
        "book": book
    }


# Get all books
@app.get("/getbooks")
def get_books():
    return {
        "books": books
    }


# JSON format for adding a book:
#
# {
#     "title": "Python Basics",
#     "author": "John"
# }