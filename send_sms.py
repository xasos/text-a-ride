from twilio.rest import TwilioRestClient
from flask import Flask, request, redirect
import twilio.twiml
from uberpy import Uber
from geopy.geocoders import Nominatim
import pdb

SECRET_KEY = "asdfasdfasdf"

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC50a25b43c9f2c9a844fe0e06a6349303"
auth_token  = "bfdcce4ecda50fa055876750bb165676"
client = TwilioRestClient(account_sid, auth_token)

counter = 0
address = ""
selected_uber = ""
latitude = ""
longitude = ""

messages = [
"Welcome to rideText! What would you like to do?",
#"A 128-bit secured webpage will now open up, where you can enter your username and password",
"Please type in an address or intersection",
"Ubers available:",
"Uber is on the way! Text the keyword 'status' for the status of your uber"
]

keywords = [
"request"
"status",
"cancel"
]

uber = Uber("gnccLgkxBcZJMca3pp9mydlSYaATAAFF", "VxhO24omuwWB-2zy3FXbCjJbpshGokmWdyjffQLY", "hKA5OENDNCaEKPFZDlqbI-YxkeRFbt7DazOVZMK_")

geolocator = Nominatim()
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    global counter
    global address
    global selected_uber
    global latitude
    global longitude
    resp = twilio.twiml.Response()
    response_details = request.values
    body = str(response_details.getlist('Body')[0])
    #pdb.set_trace()

    if counter == 0:
      resp.message(messages[0])
    if counter == 2:
      selected_uber = body
      resp.message(messages[3])
    if counter == 1:
      address = body
      latitude_longitude(address)
      counter = 2
      resp.message(messages[2])
      print(uber.get_products(latitude, longitude))
    if body.lower() == "request":
      resp.message(messages[1])
      counter = 1
    if body.lower() == "cancel":
      counter = 0
    if body.lower() == "status":
      uber_status
    return str(resp)

def local_ubers(latitude, longitude):
  return uber.get_products(latitude, longitude)

def latitude_longitude(address):
  location = geolocator.geocode(address)
  latitude = location.latitude
  longitude = location.longitude

def uber_status():
  return 3

if __name__ == "__main__":
    app.run(debug=True)

