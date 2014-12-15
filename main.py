import bottle
from bottle import Bottle, template

bottle.DEBUG = True
bottle = Bottle()
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@bottle.route('/')
def home():
    numbers = ['0426883141']
    return template('index', numbers)

def main():
  debug(True)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'