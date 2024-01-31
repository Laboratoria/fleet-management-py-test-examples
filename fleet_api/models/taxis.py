# pylint: disable=invalid-name
from ..database.db import get_connection

# https://pylint.readthedocs.io/en/stable/user_guide/messages/refactor/too-few-public-methods.html

class TaxiModel():
    @classmethod
    def get_taxis(cls, page=1, per_page=10):
        offset = (page - 1) * per_page

        try:
            connection = get_connection()
            taxis = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT * from TAXIS
                                LIMIT %s OFFSET %s""", (per_page, offset))
                resultset = cursor.fetchall()

                taxis = [{'id': row[0], 'plate': row[1]} for row in resultset]

            connection.close()
            return taxis
        except Exception as ex:
             # pylint: disable=raise-missing-from,broad-exception-raised
            raise Exception(ex)