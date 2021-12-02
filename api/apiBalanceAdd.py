from flask.wrappers import Response
from utils import *
from flask import jsonify


def balanceAdd(cardNumber: str, balanceToAdd: str) -> tuple:
    try:
        print("Function to add balance to card")
        connection = getDatabaseConnection()
        cur = connection.cursor()
        # uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'

        cur.execute(
            """update metrocards set "Balance" = "Balance" + (%s) where "CardNumber" = (%s);""",
            (balanceToAdd, cardNumber))

        connection.commit()
        cur.close()
        connection.close()

        return (jsonify(response_code=1), 200)
    except Exception as e:
        return (jsonify(response_code=-1), 500)
