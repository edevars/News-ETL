# Routes handling
from unicodedata import normalize

# Cleaning process
import re
from nltk.corpus import stopwords
import numpy as np
import pandas as pd

# Tokenizing process
import nltk
from pathlib import Path
import os

# Console logs
import logging
logging.basicConfig(level=logging.INFO)

# Global variables
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'clean_data') 


def get_routes():
    extracted_data = Path('./extracted_data').rglob('*.json')
    json_routes = [str(route) for route in extracted_data]
    names = [route.replace('extracted_data/', '') for route in json_routes]
    return [names, json_routes]


def create_df(route):
    df = pd.read_json(route)
    logging.info('Creating DataFrame')
    empty_text_index = list(df[df['article_text'] == ''].index)
    df.drop(index=empty_text_index, inplace=True)
    return df


def tokenize_column(df, column_name='article_text'):
    logging.info('Cleaning DataFrame')
    stop_words = set(stopwords.words('spanish'))

    tokenized_text = (df.apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
                      .apply(lambda tokens: [token for token in tokens if token.isalpha()])
                      .apply(lambda tokens: [token.lower() for token in tokens])
                      .apply(lambda word_list: [word for word in word_list if word not in stop_words])
                      .apply(lambda word_list: ','.join(word_list))
                      .apply(lambda answer_string:
                             re.sub(
                                 r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                                 normalize("NFD", answer_string), 0, re.I)
                             ))

    df[column_name] = tokenized_text

def create_directory():
    try: 
        os.mkdir(OUTPUT_PATH)
        logging.info('Directory clean_data created')
    except OSError as error: 
        print(error)  

def create_files():
    [names, routes] = get_routes()

    for idx, route in enumerate(routes):
        logging.info(
            f'Starting the cleaning process in the file: {names[idx]}')
        df = create_df(route)
        tokenize_column(df, 'article_text')
        doc_name = f'clean_{names[idx].replace(".json", "")}.csv'
        logging.info(f'Saving DataFrame as {doc_name}')
        df.to_csv('clean_data/' + doc_name)


if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('punkt')
    create_directory()
    create_files()

