from os import system
import logging
logging.basicConfig(level=logging.INFO)

logging.info('Extracting Data')
system('python scripts/extract.py')
logging.info('Transforming Data')
system('python scripts/transform.py')
logging.info('Saving Data')
system('python scripts/load.py')