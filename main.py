import bottle
from bottle import Bottle, template
from config import *
from twilio.rest import TwilioRestClient
from google.appengine.api import users
from google.appengine.ext import ndb


bottle.DEBUG = True
bottle = Bottle()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def home():
    numbers = ['0426883141']
    return template('index', numbers=numbers)

def main():
  debug(True)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'

@post('/addnum')
class number(ndb.Model):
  numberds = ndb.IntegerProperty()
def addnum():
  for number in request.forms.get('phone_numbers'):
    number.numberds = number
    number.put()

@post('/anus')
clientobj = TwilioRestClient(account,token)
def send_group():
  phone_numbers = request.forms.get('phone_numbers')
  message = request.forms.get('message')
  for number in phone_numbers:
    clientobj.messages.create(to=number, from_=fromnum, body=message)
