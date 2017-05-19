from sqlalchemy.sql import func
import datetime
from json import JSONEncoder
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

Base = declarative_base(JSONEncoder)

class Poll(Base):
	__tablename__ = "Poll"
	id = Column(Integer, primary_key=True)
	question = Column(String)
	pub_date = Column(DateTime(timezone=True), default=func.now())

class Choice(Base):
	__tablename__ = "Choice"
	id = Column(Integer, primary_key=True)
	poll = Column(Integer, ForeignKey("Poll.id"), nullable=False)
	choice_text = Column(String)
	votes = Column(String)
