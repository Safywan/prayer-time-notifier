import os
import requests
from dotenv import load_dotenv

load_dotenv()


def send_notification(prayer_name, prayer_time, send_at=None):
    topic = os.environ["NTFY_TOPIC"]
    url = f"https://ntfy.sh/{topic}"

    message = f"It's time for {prayer_name} prayer {prayer_time}."

    headers = {
        "Title": f"{prayer_name} Prayer Reminder",
        "Priority": "4",
        "Tags": "alarm_clock"
    }
    
    # Scheduled delivery if a future datetime was provided
    if send_at is not None:
        if send_at.tzinfo is None or send_at.utcoffset() is None:
            raise ValueError("send_at must include a timezone")
        
        headers["At"] = str(int(send_at.timestamp()))

    response = requests.post(
        url,
        data=message,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()
