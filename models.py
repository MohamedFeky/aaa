from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from config import  Base, engine


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    isbn = Column(String(13))
    genre = Column(String(50))
    publication_date = Column(Date)
    status = Column(String(50))  # Add a status field (available, loaned out, etc.)

    loans = relationship("Loan", backref="book")  # Relationship with Loans table


class Member(Base):
    __tablename__ = "members"

    member_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    contact_info = Column(String(255))
    registration_date = Column(Date)

    loans = relationship("Loan", backref="member")  # Relationship with Loans table


class Loan(Base):
    __tablename__ = "loans"

    loan_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    member_id = Column(Integer, ForeignKey("members.member_id"))
    borrow_date = Column(Date)
    return_date = Column(Date, nullable=True)
    overdue = Column(Boolean)  # Flag for overdue status





Base.metadata.create_all(bind=engine)