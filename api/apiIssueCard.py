from flask.wrappers import Response
from utils import *
from flask import jsonify
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta


def issueLimited(initialBalance: float) -> tuple:
    try:

        print("Function to issue limited")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        currentDate = datetime.now()
        date_after_month = currentDate + relativedelta(months=1)

        cardNumber = uuid.uuid4().hex

        cur.execute(
            """INSERT INTO metrocards("CardNumber", "IssuedOn", "ExpiresOn", "Balance", "CardType") VALUES (%s, %s, %s, %s, %s);""",
            (cardNumber, currentDate, str(date_after_month), initialBalance,
             'Limited'))

        connection.commit()
        cur.close()
        connection.close()

        return (jsonify(response_code=1, cardNumber=cardNumber), 200)
    except Exception as e:
        print(e)
        return (jsonify(response_code=-1), 200)


def issueUnlimited() -> tuple:
    try:
        print("Function to issue unlimited")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        currentDate = datetime.now()
        date_after_month = currentDate + relativedelta(months=1)

        cardNumber = uuid.uuid4().hex

        cur.execute(
            """INSERT INTO metrocards("CardNumber", "IssuedOn", "ExpiresOn", "Balance", "CardType") VALUES (%s, %s, %s, %s, %s);""",
            (cardNumber, currentDate, str(date_after_month), 0, 'Unlimited'))

        connection.commit()
        cur.close()
        connection.close()

        return (jsonify(response_code=1, cardNumber=cardNumber), 200)
    except Exception as e:
        return (jsonify(response_code=-1), 500)