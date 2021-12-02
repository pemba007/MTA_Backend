from flask.wrappers import Response
from utils import *
from flask import jsonify


def balanceCheck(uuid: str) -> tuple:
    try:

        connection = getDatabaseConnection()
        cur = connection.cursor()
        # uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'
        cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
                    (uuid, ))
        records = cur.fetchall()
        # print("These are the records")
        # print(records)

        connection.commit()
        cur.close()
        connection.close()

        if len(records) == 0:
            # No records
            return (jsonify(response_code=0), 200)
        else:
            return (jsonify(response_code=1, balance=records[0][3]), 200)
    except Exception as e:

        return (jsonify(response_code=-1), 500)
