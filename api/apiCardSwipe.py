# from flask.wrappers import Response
from utils import *
from flask import jsonify
from datetime import datetime


def cardSwipeMetro(cardNumber: str) -> tuple:
    try:
        print("Function to handle card swipe for metro cards")
        connection = getDatabaseConnection()
        cur = connection.cursor()
        # uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'

        # cur.execute(
        #     """update metrocards set "Balance" = "Balance" + (%s) where "CardNumber" = (%s);""",
        #     (balanceToAdd, cardNumber))

        # Step 1 : Check if balance can be handled
        # cur.execute(
        #     """select * from metrocards where "CardNumber" = '(%s)';""",
        #     (cardNumber))
        cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
                    (cardNumber, ))

        records = cur.fetchone()
        # print(records)

        if not records:
            # If no records found
            returnObject = (jsonify(response_code=-1,
                                    response_message="Not records found"), 200)
        else:
            # If records found
            isLimited = records[-1] != "Unlimited"
            hasBalance = records[-2] > 2.75
            isValid = records[-3] < datetime.now()

            if not isLimited and isValid:
                # Unlimited Card Handled
                returnObject = (jsonify(response_code=1), 200)

                # Remaining
                # Implement genenric record adding function

                # Implement Unlimited valid card handling
            elif not isLimited and not isValid:
                # Unlimited but expired

                # Remaining
                # Return Error for expired card
                returnObject = (jsonify(response_code=-1), 200)
            elif isLimited and hasBalance:
                # Limited and hasBalance

                # Remaining
                # Handle balance cut and record addition
                returnObject = (jsonify(response_code=0), 200)
            elif isLimited and not hasBalance:
                # Limited and not enough balance

                # Remaining
                # Return Error for no balance
                # Request for balance addition
                returnObject = (jsonify(response_code=-1), 200)

        # Step 2 : Cut the balance

        connection.commit()
        cur.close()
        connection.close()

        return returnObject
    except Exception as e:
        print("Exception")
        print(e)
        return (jsonify(response_code=-1), 500)


def cardSwipeDebitCredit(cardNumber: str) -> tuple:
    try:
        print("Function to handle card swipe for debit/credit cards")
        connection = getDatabaseConnection()
        cur = connection.cursor()
        # uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'

        # cur.execute(
        #     """update metrocards set "Balance" = "Balance" + (%s) where "CardNumber" = (%s);""",
        #     (balanceToAdd, cardNumber))

        # Step 1 : Check if balance can be handled
        cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
                    (cardNumber))

        records = cur.fetchone()
        print(records)
        # Step 2 : Cut the balance

        connection.commit()
        cur.close()
        connection.close()

        return (jsonify(response_code=1), 200)
    except Exception as e:
        return (jsonify(response_code=-1), 500)
