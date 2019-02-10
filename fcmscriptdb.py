# Send to single device.
from pyfcm import FCMNotification
import psycopg2

conn = psycopg2.connect(database = "testdb2", user = "postgres", password = "namespace1", host = "127.0.0.1", port = "5432")
print ('Opened database successfully')
cur = conn.cursor()

cur.execute("SELECT name  from COMPANY")
rows = cur.fetchall()
for row in rows:

   print ("NAME = ", row[0])
   name = row[0]
print ("fetched successfully");

push_service = FCMNotification(api_key="AAAALZRFb04:APA91bEjxns-acpzgQwQK93ePXeb0LfQ6oES0dW7PSTuSE00qzsWhmVqFu4M0O-D6XVH1Cb_XC2miS0AitRImEcRjSEzRKKXJAAbOJg876mOwIY04VdOiZgoi0VL5MoTWmcr1RTpN5ht")

registration_id = "dyWTx-v3YtQ:APA91bHVf4yLwu2HpflWNW9yjVX8G3mZmamMgZjqBV-pPMvQCwAydPuQUrRjxz_OZOgrO_IJr5nq2TMLZtI2fgnAu2oDV1dFvu2RC4hmyiFK2WgdZcdQYPATcbMW3Q_tHXU9D9VrEaWz"
message = name
result = push_service.notify_single_device(registration_id=registration_id, message_body=message)
print (result)
