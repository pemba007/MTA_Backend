from flask import Flask, request
from api import apiBalanceAdd, apiBalanceCheck

app = Flask(__name__)

# @app.route("/", methods=['GET'])
# def entry_api():
#     try:

#         conn = psycopg2.connect(database="MTA_Test",
#                                 user='postgres',
#                                 password='    ',
#                                 host='127.0.0.1',
#                                 port='5432')
#         cur = conn.cursor()
#         # Execute a command: this creates a new table
#         # cur.execute(
#         #     "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
#         # )

#         # Pass data to fill a query placeholders and let Psycopg perform
#         # the correct conversion (no more SQL injections!)
#         cur.execute("INSERT INTO Cards (CardType) VALUES (%s)", ("Unlimited"))

#         # Query the database and obtain data as Python objects
#         cur.execute("SELECT * FROM Cards;")
#         records = cur.fetchone()
#         print(records)
#         # Make the changes to the database persistent
#         conn.commit()

#         # Close communication with the database
#         cur.close()
#         conn.close()
#         return records
#     except Exception as err:
#         print(err)
#         return 'Error has occured'


@app.route("/test", methods=['GET', 'POST', 'DELETE'])
def testApi():
    if request.method == 'POST':
        return "This is a POST request for testing"
    else:
        return "This is a GET request for testing"


@app.route("/balance_check", methods=['GET'])
def balanceCheck():
    """Function to check the balance"""
    print("Called Balance Check")
    uniqueId = request.args.get('uuid')
    if not uniqueId:
        return "Missing Parameters", 400
    else:
        response = apiBalanceCheck.balanceCheck(uniqueId)
        return response[0], response[1]


@app.route("/balance_add", methods=['POST'])
def balanceAdd():
    """Function to add the balance"""
    print("Called Balance Add")

    cardNumber = request.args.get('cardNumber')
    balanceToAdd = request.args.get('balanceToAdd')

    # print("Unique Id", cardNumber)

    if not cardNumber or not balanceToAdd:
        return "Missing Parameters", 400
    else:
        response = apiBalanceAdd.balanceAdd(cardNumber, balanceToAdd)
        return response[0], response[1]


if __name__ == '__main__':
    app.run(debug=True)
