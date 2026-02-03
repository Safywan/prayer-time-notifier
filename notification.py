import http.client
import urllib
import os
# Function that sends notification to phone using pushover API
def prayer_time_notification(prayer_times, curr_time):
    # Get pushover credentials from environment variables
    token = os.environ["PUSHOVER_TOKEN"]
    user = os.environ["PUSHOVER_USER"]
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": token,
                     "user": user,
                     "message": "The time right now is " + curr_time + " It's time for " + prayer_times[curr_time] + " prayer."
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()




