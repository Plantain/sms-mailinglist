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
    return template('index')

def main():
  debug(True)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'

@bottle.route('/add_numbers')
def add_numbers():
  class number(ndb.Model):
    numberds = ndb.IntegerProperty()
  for number in request.forms.get('phone_numbers'):
    number.numberds = number
    number.put()
  return template('add_numbers')

@bottle.route('/list_numbers')
def show_numbers():
  return template('list_numbers', numbers=['0234'])

@bottle.route('/send_message')
def send_message():
  phone_numbers = [request.query.phone_numbers]
  message = request.query.message
  for number in phone_numbers:
    clientobj.messages.create(to="+" + number, from_=fromnum, body=message)
  return template('send_message')
