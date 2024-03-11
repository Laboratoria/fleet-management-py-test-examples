import os
from psycopg2 import OperationalError, connect

def get_connection():
    try:
        return connect(
            host=os.getenv("POSTGRES_HOST"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DATABASE"),
        )
    except OperationalError as ex:
        print_db_exception(ex)
        return None

def print_db_exception(ex):
    print(f"pgcode: {ex.pgcode} pgerror: {ex.pgerror}")
    raise ex from ex
