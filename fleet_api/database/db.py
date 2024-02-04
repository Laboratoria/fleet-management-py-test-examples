import os
from psycopg2 import DatabaseError, connect


def get_connection():
    try:
        return connect(
            host=os.getenv("POSTGRES_HOST"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DATABASE"),
        )
    except DatabaseError as ex:
        raise ex
