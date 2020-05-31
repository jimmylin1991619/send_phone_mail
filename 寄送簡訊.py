# https://www.twilio.com/docs/python/install
from twilio.rest import Client

#Your Account SID from twilio.com/console
account_sid = "ACadde386b8e51d4b3981e6e0639e29599"
#Your Auth Token from twilio.com/console
auth_token = "d0174ae665c87aa0c54e4111ceb2b1ea"

client = Client(account_sid, auth_token)

message = client.messages.create(
	to="+886932985201",
	from_="+13304734561",
	body="大家好")

print(message.sid)



