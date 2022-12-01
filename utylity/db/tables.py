from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

Base = declarative_base()


class BaseItem(Base):
    __tablename__ = 'BaseItem'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    category = Column(String(60))
    content = Column(String(1000), nullable=False)
    type = Column(String(60), nullable=False)
    path_source = Column(String(600))
    path_destination = Column(String(600))
    status = Column(Boolean, nullable=False)
    cooldown = Column(Integer)
    time_limit = Column(DateTime)
    data = Column(String(60))
