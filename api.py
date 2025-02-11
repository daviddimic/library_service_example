from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models import Author, Book
from typing import List
import crud

router = APIRouter()

@router.post("/authors/", response_model=Author)
def create_author(name: str, session: Session = Depends(get_session)):
    return crud.create_author(session, name)

@router.post("/books/", response_model=Book)
def create_book(title: str, author_id: int, session: Session = Depends(get_session)):
    return crud.create_book(session, title, author_id)

@router.get("/authors/", response_model=List[Author])
def get_authors(session: Session = Depends(get_session)):
    return crud.get_authors(session)

@router.get("/author/{author_id}", response_model=Author)
def get_author(author_id: int, session: Session = Depends(get_session)):
    return crud.get_author(session, author_id)

@router.get("/books/", response_model=List[Book])
def get_books(session: Session = Depends(get_session)):
    return crud.get_books(session)

@router.get("/book/{book_id}", response_model=Book)
def get_book(book_id: int, session: Session = Depends(get_session)):
    return crud.get_book(session, book_id)

@router.delete("/authors/{author_id}")
def delete_author(author_id: int, session: Session = Depends(get_session)):
    if crud.delete_author(session, author_id):
        return {"message": "Author deleted"}
    return {"error": "Author not found"}

