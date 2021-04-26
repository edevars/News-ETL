# DB Management
from db.connection import DataBase
from db.models.article import Article

# Files handling
import pandas as pd
from pathlib import Path
import os


def get_clean_data():
    cleaned_data = Path('./clean_data').rglob('*.csv')
    file_paths = [str(route) for route in cleaned_data]
    names = [route.replace('clean_data/', '') for route in file_paths]
    return [names, file_paths]

def get_articles_dict(path):
    df = pd.read_csv(path);
    df = df[['url','title','article_text']]
    articles_dict = df.to_dict('records')
    return articles_dict

def save_to_db(db,articles):
    for article in articles:
        Article.save_article(db, article)

if __name__ == '__main__':
    db = DataBase.engine()
    [names, file_paths] = get_clean_data()
    for path in file_paths:
        articles = get_articles_dict(path)
        save_to_db(db, articles)








