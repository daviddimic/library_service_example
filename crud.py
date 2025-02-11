from sqlmodel import select, Session
from models import Author, Book

def create_author(session: Session, name: str):
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.refresh(author)
    return author

def create_book(session: Session, title: str, author_id: int):
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def get_authors(session: Session):
    return session.exec(select(Author)).all()

def get_author(session: Session, author_id: int):
    return session.get(Author, author_id)

def get_books(session: Session):
    return session.exec(select(Book)).all()

def get_book(session: Session, book_id: int):
    return session.get(Book, book_id)

def delete_author(session: Session, author_id: int):
    author = session.get(Author, author_id)
    if author:
        session.delete(author)
        session.commit()
        return True
    return False

