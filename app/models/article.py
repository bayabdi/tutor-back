from app.db.base_class import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship


class Article(Base):
    """
    Database model for an Article
    """
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    titles = relationship("ArticleTitle", back_populates="article")