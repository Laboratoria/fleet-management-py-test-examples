from psycopg2 import DataError, DatabaseError, OperationalError
from ..database.db import get_connection, print_db_exception
# import pdb

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
