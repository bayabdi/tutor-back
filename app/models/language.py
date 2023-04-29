from app.db.base_class import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship


class Language(Base):
    """
    Database model for an language
    """
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), index=True, nullable=False)
    name = Column(String(255))
    category_names = relationship('CategoryName', back_populates='language')
    article_titles = relationship('ArticleTitle', back_populates='language')