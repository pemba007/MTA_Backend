import uuid

from datetime import datetime
import psycopg2.extras


def balanceCut(connectionCursor, cardNumber) -> bool:
    """Utility function to cut balance"""
    print("Cutting balace")
    print(type(cardNumber))
    try:

        connectionCursor.execute(
            """update metrocards set "Balance" = "Balance" - 2.75 where "CardNumber" = (%s);""",
            (cardNumber, ))
        return True
    except Exception as e:
        print("Exception : Cutting balace")
        print(e)
        return False


def addRecord(connectionCursor, cardNumber, paymentType) -> bool:
    """Utility function to add record to the record table"""

    psycopg2.extras.register_uuid()
    print("Called add Records")
    try:

        connectionCursor.execute(
            """INSERT INTO payment("TransactionID", "CardNumber", "TimeofPayment", "PaymentType") VALUES (%s, %s, %s, %s);""",
            (uuid.uuid4(), cardNumber, datetime.now(), paymentType))

        # connectionCursor.execute(sqlStatement)
        return True
    except Exception as e:
        print(e)
        return False
