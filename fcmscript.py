# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAALZRFb04:APA91bEjxns-acpzgQwQK93ePXeb0LfQ6oES0dW7PSTuSE00qzsWhmVqFu4M0O-D6XVH1Cb_XC2miS0AitRImEcRjSEzRKKXJAAbOJg876mOwIY04VdOiZgoi0VL5MoTWmcr1RTpN5ht")

registration_id = "dyWTx-v3YtQ:APA91bHVf4yLwu2HpflWNW9yjVX8G3mZmamMgZjqBV-pPMvQCwAydPuQUrRjxz_OZOgrO_IJr5nq2TMLZtI2fgnAu2oDV1dFvu2RC4hmyiFK2WgdZcdQYPATcbMW3Q_tHXU9D9VrEaWz"
message = "Hi john, your Uber driver is around"
result = push_service.notify_single_device(registration_id=registration_id, message_body=message)
print (result)
