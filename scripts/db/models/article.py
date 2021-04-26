from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
logging.basicConfig(level=logging.INFO)

base = declarative_base()

class Article(base):
    __tablename__ = 'news'

    article_id = Column(UUID(as_uuid=True), primary_key=True)
    url = Column(String)
    title = Column(String)
    article_text = Column(String)

    def save_article(db, article):
        Session = sessionmaker(db)
        session = Session()
        base.metadata.create_all(db)

        saved_article = Article(article_id=article['article_id'], 
                                url=article['url'],
                                title=article['title'], 
                                article_text=article['article_text'])
        session.add(saved_article)
        session.commit()
        logging.info(f"Article saved with UUID {article['article_id']}")
