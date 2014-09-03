# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
# Need to change these credentials 
account_sid ="ACacc3cd1f26418f78dd415ef0454924be"
auth_token = "bd47541aec30109464db256def130777"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+19252197076", from_="+14157128352",
                                     body="Hey there! Thanks for your interest in Dattch! For an iOS download: LINK; For an Andriod download: LINK" 
