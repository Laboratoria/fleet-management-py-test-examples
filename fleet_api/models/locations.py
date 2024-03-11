from psycopg2 import DataError, DatabaseError, OperationalError
from ..database.db import get_connection, print_db_exception
# import pdb

ROWS_PER_PAGE = 10

def get_limit_offset_query(page, per_page):
    """ Returns a string with the LIMIT and OFFSET query parts
    based on the page and per_page parameters """
    query_parts = []
    if per_page:
        query_parts.append(f"LIMIT {per_page}")
    if page:
        offset = (page - 1) * per_page
        query_parts.append(f"OFFSET {offset}")
    return " ".join(query_parts)

def get_last_locations(page, per_page=ROWS_PER_PAGE):
    try:
        offset_limit = get_limit_offset_query(page, per_page)
        connection = get_connection()
        locations = []
        with connection.cursor() as cursor:
            # thank you copilot
            cursor.execute("""
            SELECT taxis.*, latest_trajectories.*
            FROM taxis
            INNER JOIN (
                SELECT trajectories.*
                FROM trajectories
                INNER JOIN (
                    SELECT taxi_id, MAX(date) as max_date
                    FROM trajectories
                    GROUP BY taxi_id
                ) as max_dates ON trajectories.taxi_id = max_dates.taxi_id AND trajectories.date = max_dates.max_date
            ) as latest_trajectories ON taxis.id = latest_trajectories.taxi_id
            """ + offset_limit)
            resultset = cursor.fetchall()
            locations = [{
                "id": row[0],
                "plate": row[1],
                "timestamp": row[4].timestamp(),
                "lat": row[5],
                "lon": row[6]}
                for row in resultset]
        connection.close()
        return locations
    # https://www.psycopg.org/docs/errors.html
    # cual error debemos usar DataError, DatabaseError, OperationalError?
    except (DataError, DatabaseError, OperationalError) as ex:
        print_db_exception(ex)
        return None

def get_locations_by_taxi_id(taxi_id, page, per_page, date=None):
    offset = (page - 1) * per_page
    try:
        connection = get_connection()
        locations = []
        with connection.cursor() as cursor:
            # date = datetime.date(2008, 2, 8) and in the table its a timestamp,
            # so need to query the whole day
            # (1, 6418, datetime.datetime(2008, 2, 2, 14, 22, 40), 116.30508, 39.96525)
            # https://stackoverflow.com/questions/18269966/determine-if-a-given-timestamp-is-within-the-same-day-in-postgresql
            cursor.execute(
                """SELECT * FROM trajectories WHERE (date >= %s and date < %s + interval '1 day')
                and taxi_id=%s LIMIT %s OFFSET %s""",
                (date, date, taxi_id, per_page, offset),
            )
            resultset = cursor.fetchall()
            locations = [
                {
                    "id": row[0],
                    "plate": row[1],
                    "timestamp": row[2].timestamp(),
                    "lat": row[3],
                    "lon": row[4],
                }
                for row in resultset
            ]
        connection.close()
        return locations
    except (DataError, DatabaseError, OperationalError) as ex:
        print_db_exception(ex)
        return None
