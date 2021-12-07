# from flask.wrappers import Response
from utils import *
from flask import jsonify
from datetime import datetime
from api import apiUtils


def cardSwipeMetro(cardNumber: str) -> tuple:
    try:
        print("Function to handle card swipe for metro cards")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
                    (cardNumber, ))

        records = cur.fetchone()
        print("Records got" + str(records))

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
                print("Unlimited Valid Card")
                returnObject = (jsonify(response_code=1), 200)

                if (apiUtils.addRecord(cur,
                                       cardNumber=cardNumber,
                                       paymentType="Metrocard")):
                    connection.commit()
                    returnObject = (jsonify(response_code=1), 200)
                else:
                    returnObject = (jsonify(response_code=-1), 200)
                # Remaining
            elif not isLimited and not isValid:
                print("Unlimited invalid Card")

                # Remaining
                # Return Error for expired card
                returnObject = (jsonify(response_code=-1), 200)
            elif isLimited and hasBalance:
                # Limited and hasBalance
                print("Limited balance card")

                if (apiUtils.balanceCut(cur, cardNumber=cardNumber)):

                    if (apiUtils.addRecord(cur,
                                           cardNumber=cardNumber,
                                           paymentType="Metrocard")):
                        connection.commit()
                        returnObject = (jsonify(response_code=1), 200)
                    else:
                        connection.rollback()
                        returnObject = (jsonify(
                            response_code=-1,
                            response_message="Couldn't add record"), 200)
                else:
                    connection.rollback()
                    returnObject = (jsonify(response_code=-1), 200)

            elif isLimited and not hasBalance:
                # Limited and not enough balance
                print("Limited no balance card")

                returnObject = (jsonify(response_code=-1,
                                        response_message="Not enough balance"),
                                200)

        # Step 2 : Cut the balance
        cur.close()
        connection.close()

        return returnObject
    except Exception as e:
        print("Exception")
        print(e)
        return (jsonify(response_code=-1), 500)


def cardSwipeDebitCredit(debitCreditCardNumber: str) -> tuple:
    try:
        print("Function to handle card swipe for debit/credit cards")
        connection = getDatabaseConnection()
        cur = connection.cursor()

        # Put record for the cards
        if (apiUtils.addRecord(cur,
                               cardNumber=debitCreditCardNumber,
                               paymentType="Debit/Credit")):
            connection.commit()
            returnObject = (jsonify(response_code=1), 200)
        else:
            returnObject = (jsonify(response_code=-1), 200)

        connection.commit()
        cur.close()
        connection.close()

        return returnObject
    except Exception as e:
        return (jsonify(response_code=-1), 500)
