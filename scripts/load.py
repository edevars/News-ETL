from db.connection import DataBase
from db.models.article import Article

db = DataBase.engine()

# Article
article = {'article_id': "40e6215d-b5c6-4896-987c-f30f3678f608",
           'url': "Example", 
           'title': "article title", 
           'article_text': "somebody loves me"}

Article.save_article(db, article)
