import config.py
from twilio.rest import TwilioRestClient

class sms:
  def __init__:
    self.account =
    self.token = ""
    self.clientobj = TwilioRestClient(account,token)

  def send_group(self, numbers, message):
    for number in numbers:
      self.clientobj.messages.create(to=number, from_=config.fromnum, body=message)
