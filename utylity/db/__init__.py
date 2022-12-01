from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

engine = db.create_engine('sqlite:///store.db')

Session = sessionmaker(bind=engine)
session = Session()
