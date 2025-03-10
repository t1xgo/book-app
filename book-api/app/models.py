import uuid
from sqlalchemy import Column, String, Boolean
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    read = Column(Boolean, default=False)
