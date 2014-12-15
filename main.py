import bottle
from bottle import Bottle, route, request, response, template
from twilio.rest import TwilioRestClient
from google.appengine.api import users
from google.appengine.ext import ndb
from config import *


clientobj = TwilioRestClient(account,token)

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

@bottle.post('/addnum')
class number(ndb.Model):
  numberds = ndb.IntegerProperty()
def addnum():
  for number in request.forms.get('phone_numbers'):
    number.numberds = number
    number.put()

@bottle.get('/anus')
def send_group():
  phone_numbers = [request.query.phone_numbers]
  message = request.query.message
  for number in phone_numbers:
    clientobj.messages.create(to=number, from_=fromnum, body=message)
  return 'omg it worked'
