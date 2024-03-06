import requests
import os
from twilio.rest import Client

OPEN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "14e3c76522b8a054496419cd31088461"
account_sid = "ACf25a017b61fa3d812c562ceed912cb49"#os.environ['TWILIO_ACCOUNT_SID']
auth_token = "63f4941b4110ae53b6128a0698a03101"#os.environ['TWILIO_AUTH_TOKEN']

weather_params = {
    "lat": "26.920980",
    "lon": "75.794220",
    "appid": api_key,
    "cnt" : 4,

}

response = requests.get(OPEN_ENDPOINT, params=weather_params)
#print(response.status_code)
response.raise_for_status()
wether_data = response.json()

will_rain = False
for Hour_data in wether_data["list"]:
    condition_code = Hour_data["weather"][0]["id"]
    #print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going rain today. Remember to bring an ☂️",
        from_='+18593792286',
        to='+91 95282 84903'
    )
    print(message.status)

