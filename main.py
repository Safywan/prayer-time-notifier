import scraper 
import time
import datetime
import notification
import schedule
from dotenv import load_dotenv
load_dotenv()

URL = "https://awqat.com.au/mgm/"

def main():
    prayer_times = scraper.fetch_prayer_times(URL)
    #print(prayer_times)
    
    # Get the time right now
    now = datetime.datetime.now()
    curr_time = now.strftime("%-I:%M%p")
    
    if curr_time in prayer_times:
    # Send notification if the current time is in the prayer times
        notification.prayer_time_notification(prayer_times, curr_time)
        print("Notification successful!")

schedule.every(10).seconds.do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)
       