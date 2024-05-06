from sqlalchemy.orm import sessionmaker
from models import Book
from config import engine


def create_book(book):
    #add a new book record to the database
    session = sessionmaker(bind=engine)()
    session.add(book)
    session.commit()
    session.close()

def get_all_books():
    # retrieve all book records from database
    session = sessionmaker(bind=engine)()
    all_books = session.query(Book).all()
    session.close()
    return all_books

def get_book_by_id(book_id):
    # find a book by its id
    session = sessionmaker(bind=engine)()
    book = session.query(Book).filter_by(book_id=book_id).first()
    session.close()
    return book

def update_book(book_id, updates):
    # update book information based on id
    session = sessionmaker(bind=engine)()
    book = session.query(Book).filter_by(book_id=book_id).first()
    for key, value in updates.items():
        setattr(book, key, value)
    session.commit()
    session.close()

def delete_book(book_id):
    session = sessionmaker(bind=engine)()
    book = session.query(Book).filter_by(book_id=book_id).first()
    if book:
        session.delete(book)
        session.commit()
    session.close()



