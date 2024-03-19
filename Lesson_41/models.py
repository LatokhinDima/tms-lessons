from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(400))
    choices = relationship('Choice', back_populates='question')




