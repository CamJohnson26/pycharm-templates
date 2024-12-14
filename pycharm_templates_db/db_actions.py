import psycopg2
from dotenv import load_dotenv

import os

from bookmark_library.library_db.queries.get_entity_query import get_entity_query

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

database = psycopg2.connect(DATABASE_URL)


def get_entity(url):
    return get_entity_query(url, database)
