from app.db.base_class import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship


class Category(Base):
    """
    Database model for an Category
    """
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    names = relationship("CategoryName", back_populates="category")