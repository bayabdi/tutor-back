from app.db.base_class import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

class CategoryName(Base):
    __tablename__ = "category_names"
    
    id = Column(Integer, primary_key=True, index=True)
    
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    language = relationship('Language', back_populates='category_names')

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship('Category', back_populates='names')

    text = Column(String(250))
