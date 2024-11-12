from typing import List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

books_db = []

@app.post("/books")
async def create_book(book: Book):
    books_db.append(book)
    return {"message": "Book added successfully", "book": book}

@app.get("/books/{id}")
async def get_book(id: int):
    for book in books_db:
        if book.id == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{id}")
async def update_book(id: int, book: Book):
    for index, existing_book in enumerate(books_db):
        if existing_book.id == id:
            books_db[index] = book
            return {"message": "Book updated", "book": book}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}")
async def delete_book(id: int):
    for index, book in enumerate(books_db):
        if book.id == id:
            books_db.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
