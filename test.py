from flask import Flask, jsonify
from utils import *

from datetime import datetime

# Flask Run Code
# FLASK_ENV=development flask run

# now = datetime.now()
# print("Now is")
# print(now)

conn = getDatabaseConnection()
cur = conn.cursor()
cardNumber = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'
# cardType = 'Unlimited'
# insertSQL = """INSERT INTO metrocards("CardNumber", "CardType", "IssuedOn", "ExpiresOn", "Balance") VALUES ((%s), (%s), '2004-10-19 10:23:45', '2004-10-19 10:23:50', 2.80) ;"""

# cur.execute(insertSQL, (uuid, cardType))

cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
            (cardNumber, ))

records = cur.fetchone()
# print(records)

if not records:
    # If no records found
    # returnObject = (jsonify(response_code=0), 200)
    print("No Records found")
else:
    # If records found
    isLimited = records[-1] != "Unlimited"
    hasBalance = records[-2] > 2.75
    isValid = records[-3] < datetime.now()

    # print(isValid)

    # print(type(isValid))

    if not isLimited:
        print("Unlimited thing")

# print(returnObject)

# cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
#             (uuid, ))

# Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM metrocards;")
# records = cur.fetchall()
# records = (jsonify(response_code=0), 200)
# print(records)
# Make the changes to the database persistent

# conn.commit()

# Close communication with the database
cur.close()
conn.close()