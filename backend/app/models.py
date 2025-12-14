from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    execution_time = Column(Integer, nullable=False)
    status = Column(String, default="Pending")
    attempts = Column(Integer, default=0)
    logs = Column(Text, default="")
