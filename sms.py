# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
# Need to change these credentials 
account_sid ="NEED TO ADD"
auth_token = "NEED TO ADD"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+19252197076", from_="+14157128352",
                                     body="Hey there! Thanks for your interest in Dattch! For an iOS download: http://taps.io/getdattchios; For an Andriod download: http://taps.io/getdattchandroid" 
