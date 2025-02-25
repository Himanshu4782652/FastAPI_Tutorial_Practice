# Build_a_CRUD_REST_API_Response_Models_Validation_And_Exceptions

from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "python",
        "author": "anmol kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-01-01",
        "page_count": 1234,
        "language": "english",
    },
    {
        "id": 2,
        "title": "think python",
        "author": "pushkar kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-02-01",
        "page_count": 5678,
        "language": "english",
    },
    {
        "id": 3,
        "title": "python core",
        "author": "himanshu kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-03-01",
        "page_count": 9012,
        "language": "english",
    },
    {
        "id": 4,
        "title": "python advance",
        "author": "aman kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-04-01",
        "page_count": 3456,
        "language": "english",
    },
    {
        "id": 5,
        "title": "python oops",
        "author": "harsh kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-04-01",
        "page_count": 7893,
        "language": "english",
    },
    {
        "id": 6,
        "title": "python dsa",
        "author": "prinve kumar",
        "publisher": "vidyapeeth",
        "published_date": "2026-04-01",
        "page_count": 5642,
        "language": "english",
    },
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int 
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int 
    language: str

#get all books
@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


#create a book
@app.post("/books",status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book=book_data.model_dump()   #model_dump() converts book_data(which is an object) into list
    books.append(new_book)
    return new_book

#get a one book
@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id']==book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

#update a book
@app.patch("/book/{book_id}")
async def update_book(book_id:int,book_update_data=BookUpdateModel) -> dict:
    for book in books:
        if book['id']==book_id:
            book['title']=book_update_data.title
            book['publisher']=book_update_data.publisher
            book['page_count']=book_update_data.page_count
            book['language']=book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")

#delete a book
@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book["id"]==book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="book not found")
