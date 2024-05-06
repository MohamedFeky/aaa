from sqlalchemy.orm import sessionmaker
from models import Member
from config import engine

def create_member(member):
    # add a new member record to the database
    session = sessionmaker(bind=engine)()
    session.add(member)
    session.commit()
    session.close()

def get_all_members():
    # retrieve all member records from the database
    session = sessionmaker(bind=engine)()
    all_members = session.query(Member).all()
    session.close()
    return all_members

def get_member_by_id(member_id):
    # find a member by their id
    session = sessionmaker(bind=engine)()
    member = session.query(Member).filter_by(member_id=member_id).first()
    session.close()
    return member

def update_member(member_id, updates):
    # update member information based on id
    session = sessionmaker(bind=engine)()
    member = session.query(Member).filter_by(member_id=member_id).first()
    for key, value in updates.itmes():
        setattr(member, key, value)
    session.commit()
    session.close()

def delete_member(member_id):
    session = sessionmaker(bind=engine)()
    member = session.query(Member).filter_by(member_id=member_id).first()
    if member:
        member.delete(member)
        session.commit()
    session.close()