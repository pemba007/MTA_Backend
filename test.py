from flask import Flask, jsonify
from utils import *

# conn = getDatabaseConnection()
# cur = conn.cursor()
uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'
cardType = 'Unlimited'
# insertSQL = """INSERT INTO metrocards("CardNumber", "CardType", "IssuedOn", "ExpiresOn", "Balance") VALUES ((%s), (%s), '2004-10-19 10:23:45', '2004-10-19 10:23:50', 2.80) ;"""

# cur.execute(insertSQL, (uuid, cardType))

uuid = '74b83e33-cde6-4ac9-bf1f-915a9f03a54d'
# cur.execute("""select * from metrocards where "CardNumber" = (%s);""",
#             (uuid, ))

# Query the database and obtain data as Python objects
# cur.execute("SELECT * FROM metrocards;")
# records = cur.fetchall()
records = (jsonify(response_code=0), 200)
print(records)
# Make the changes to the database persistent

# conn.commit()

# Close communication with the database
# cur.close()
# conn.close()