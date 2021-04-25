from os import system
import logging
logging.basicConfig(level=logging.INFO)

logging.info('Deleting outdated extracted_data directory')
system('rm -r extracted_data')
logging.info('Executing scrapper')
system('python NewsWebScraper/news_scraper/run_spiders.py')