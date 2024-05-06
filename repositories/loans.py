from sqlalchemy.orm import sessionmaker
from models import Loan
from config import engine
from datetime import date, timedelta

def create_loan(loan):
    # create a new loan record
    session = sessionmaker(bind=engine)()
    session.add(loan)
    session.commit()
    session.close()

def get_all_loans():
    # retrieve all loan records
    session = sessionmaker(bind=engine)()
    all_loans = session.query(Loan).all()
    session.close()
    return all_loans

def get_loan_by_id(loan_id):
    # find a loan by its ID
    session = sessionmaker(bind=engine)()
    loan = session.query(Loan).filter_by(loan_id=loan_id).first()
    session.close()
    return loan

def get_all_borrowed_books():
    # Retrieve all loan records where books are not returned
    session = sessionmaker(bind=engine)()
    borrowed_books = session.query(Loan).filter_by(return_date=None).all()
    session.close()
    return borrowed_books

def search_loans(criteria):
    # Search for loans based on member name or book title (implement logic)
    session = sessionmaker(bind=engine)()
    from repositories.members import Member  # Import Member model for join (member name search)
    from repositories.books import Book  # Import Book model for join (book title search)

    loans = None
    if criteria.isdigit():
        # Search by member ID (assuming criteria is a string representation of ID)
        loans = session.query(Loan).filter_by(member_id=int(criteria)).all()
    else:
        # Search by member name (join with Members table)
        #loans = session.query(Loan).join(Member, Loan.member_id == Member.member_id).filter(Member.name.like(f"%{criteria}%")).all()
        # OR Search by book title (join with Books table)
        # Uncomment and modify if needed
        book_loans = session.query(Loan).join(Book, Loan.book_id == Book.book_id).filter(Book.title.like(f"%{criteria}%")).all()
        loans = loans + book_loans  # Combine results (consider duplicates)

    session.close()
    return loans