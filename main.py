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
    
    print("\n--- Melbourne Grand Mosque Prayer Times ---")
    
    for prayer_time, prayer_name in prayer_times.items():
        print(f"{prayer_name:<10} {prayer_time}")
        
    print("------------------------------------------")
    
    # Get the current time 
    now = datetime.datetime.now()
    curr_time = now.strftime("%-I:%M%p")
    
    if curr_time in prayer_times and prayer_times[curr_time] != "Sunrise":
    # Send notification if the current time is in the prayer times
        notification.send_notification(prayer_times[curr_time], curr_time)
        print("Notification successful!")
    else:
        print("Not time for prayer yet. Current time is " + curr_time)
# schedule.every(1).minute.do(main)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)
if __name__ == "__main__":
    main()
       