from flask import Flask, request
from flask.wrappers import Response
from api import apiBalanceAdd, apiBalanceCheck, apiCardSwipe, apiIssueCard, apiLatestPayment
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})


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
    cardNumber = request.args.get('cardNumber')
    # cardNumber = request.json['params']['cardNumber']
    if not cardNumber:
        return "Missing Parameters", 400
    else:
        response = apiBalanceCheck.balanceCheck(cardNumber)
        return response[0], response[1]


@app.route("/balance_add", methods=['POST'])
def balanceAdd():
    """Function to add the balance"""
    print("Called Balance Add")

    print(request.json['params'])

    cardNumber = request.json['params']['cardNumber']
    balanceToAdd = request.json['params']['balanceToAdd']

    # cardNumber = request.args.get('cardNumber')
    # balanceToAdd = request.args.get('balanceToAdd')

    print("cardNumber", cardNumber)
    print('balanceToAdd', balanceToAdd)

    if not cardNumber or not balanceToAdd:
        return "Missing Parameters", 400
    else:
        response = apiBalanceAdd.balanceAdd(cardNumber=cardNumber,
                                            balanceToAdd=balanceToAdd)
        return response[0], response[1]


@app.route("/card_swipe_metro", methods=['POST'])
def cardSwipeMetro():
    """Function to handle metro card swipe"""
    print("Called Metro Card Swipe")

    # cardNumber = request.args.get('cardNumber')
    cardNumber = request.json['params']['cardNumber']

    response = apiCardSwipe.cardSwipeMetro(cardNumber=cardNumber)

    return response[0], response[1]


@app.route("/card_swipe_debit_credit", methods=['POST'])
def cardSwipeDebitCredit():
    """Function to handle debit/credit card pay"""
    print("Called Debit / Card Card Swipe")

    # cardNumber = request.args.get('cardNumber')
    cardNumber = request.json['params']['cardNumber']

    response = apiCardSwipe.cardSwipeDebitCredit(
        debitCreditCardNumber=cardNumber)

    return response[0], response[1]


@app.route("/issue_metro_limited", methods=['POST'])
def issueMetroLimited():
    """Function to issue limited metro card"""

    # initialBalance = request.args.get('initialBalance')
    initialBalance = request.json['params']['initialBalance']

    response = apiIssueCard.issueLimited(initialBalance=initialBalance)

    return response[0], response[1]


@app.route("/issue_metro_unlimited", methods=['POST'])
def issueMetroUnlimited():
    """Function to issue unlimited metro card"""

    response = apiIssueCard.issueUnlimited()

    return response[0], response[1]


@app.route('/get_latest_payments', methods=['GET'])
def getLatestPayment():
    """Function to get latest payment"""

    response = apiLatestPayment.getLatestPayment()

    return response[0], response[1]


@app.route('/get_latest_metrocards', methods=['GET'])
def getLatestMetrocards():
    """Function to get latest metrocards"""

    response = apiLatestPayment.getLatestCards()

    return response[0], response[1]


if __name__ == '__main__':
    app.run(debug=True)
