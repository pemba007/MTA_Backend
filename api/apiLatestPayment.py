from flask.wrappers import Response
from utils import *
from flask import jsonify
import uuid
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
import json


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


def getLatestPayment() -> tuple:
    try:
        print("Function to get latest payment")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        cur.execute(
            """select * from payment ORDER BY "TimeofPayment" desc limit 3""")
        records = cur.fetchall()
        print(type(records))
        print(records)
        temp = []
        for x in records:
            t = []
            for y in x:
                if isinstance(y, (datetime, date, time)):
                    t.append(y.isoformat())
                else:
                    t.append(y)
            temp.append(t)
        print(temp)

        connection.commit()
        cur.close()
        connection.close()
        return (jsonify(response_code=1, records=temp), 200)
    except Exception as e:
        print(e)
        return (jsonify(response_code=1), 200)


def getLatestCards() -> tuple:
    try:
        print("Function to get latest cards")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        cur.execute(
            """select * from metrocards ORDER BY "IssuedOn" desc limit 3""")

        records = cur.fetchall()
        print(type(records))
        print(records)
        temp = []
        for x in records:
            temp.append(list(x))
        connection.commit()
        cur.close()
        connection.close()
        return (jsonify(response_code=1, records=temp), 200)
    except Exception as e:
        print(e)
        return (jsonify(response_code=1), 200)
