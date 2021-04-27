# News ETL Process

A repository developed with Scrapy, Python and SQL Alchemy to extract articles from top news website in Mexico.

## Installation

Clone this repository and install with conda the environment

```bash
conda env create -f environment.yml
```

Then activate it with:

```bash
conda activate news_etl_process
```

Finally fill the environment variables to connect with your Postgres database in a `.env` file. This variable you can find it in the `.env.example` file provided in this repository. 

```
DB_USER=youruser
DB_PASSWORD=adminsupercool2021
DB_NAME=cool_database
DB_SERVER=127.0.0.1
DB_PORT=5432
```

## Running the ETL Process

To start the ETL process only run:

```bash
python pipeline.py
```