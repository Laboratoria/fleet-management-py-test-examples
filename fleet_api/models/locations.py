from ..database.db import get_connection

ROWS_PER_PAGE = 10


def get_locations(taxi_id, page, per_page):
    offset = (page - 1) * per_page
    try:
        connection = get_connection()
        locations = []
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM trajectories WHERE Taxi_id='%s' LIMIT %s OFFSET %s""",
                (taxi_id, per_page, offset),
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
    except Exception as ex:
        # pylint: disable=raise-missing-from,broad-exception-raised
        raise Exception(ex)
