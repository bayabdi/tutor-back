from app.db.base_class import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

class ArticleTitle(Base):
    __tablename__ = "article_titles"
    
    id = Column(Integer, primary_key=True, index=True)
    
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    language = relationship('Language', back_populates='article_titles')

    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    article = relationship('Article', back_populates='titles')

    text = Column(String(500))
