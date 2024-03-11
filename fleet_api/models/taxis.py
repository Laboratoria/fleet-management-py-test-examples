from ..database.db import get_connection, print_db_exception

def get(page, per_page):
    offset = (page - 1) * per_page

    try:
        connection = get_connection()
        taxis = []
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * from TAXIS
                            LIMIT %s OFFSET %s""",
                (per_page, offset),
            )
            resultset = cursor.fetchall()
            taxis = [{"id": row[0], "plate": row[1]} for row in resultset]

        connection.close()
        return taxis
    # https://www.psycopg.org/docs/errors.html
    # cual error debemos usar DataError, DatabaseError, OperationalError?
    # pylint: disable=broad-except
    except Exception as ex:
        # pylint: disable=raise-missing-from,broad-exception-raised
        print_db_exception(ex)
        return None
