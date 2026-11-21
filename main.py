import datetime
import sys
from zoneinfo import ZoneInfo

import scraper
import notification

URL = "https://awqat.com.au/mgm/"
TIMEZONE = ZoneInfo("Australia/Melbourne")

EXPECTED_PRAYERS = {
    "Fajr", "Sunrise", "Dhuhr",
    "Asr", "Maghrib", "Isha"
}


def main(dry_run=False):
    prayer_times = scraper.fetch_prayer_times(URL)

    # Check for all expected prayers successfully scraped
    if (len(prayer_times) != 6 or
            set(prayer_times.values()) != EXPECTED_PRAYERS):
        raise ValueError("Invalid prayer data. Nothing scheduled.")

    now = datetime.datetime.now(TIMEZONE)
    upcoming = []

    print(f"\nPrayer schedule for {now.date()}")

    for prayer_time, prayer_name, in prayer_times.items():

        # Skip sunrise
        if prayer_name == "Sunrise":
            continue

        # Convert the string into a time object for ntfy
        parsed_time = datetime.datetime.strptime(
            prayer_time, "%I:%M%p"
        ).time()

        # Combine today's date, prayer time, and timezone
        send_at = datetime.datetime.combine(
            now.date(), parsed_time, tzinfo=TIMEZONE
        )

        # Don't schedule prayers that have already passed
        if send_at <= now:
            print(f"SKIPPED: {prayer_name} - {prayer_time}")
            continue

        upcoming.append((prayer_name, prayer_time, send_at))

    # Schedule each upcoming prayer
    for prayer_name, prayer_time, send_at in upcoming:
        if dry_run:
            print(f"WOULD SCHEDULE: {prayer_name} - {prayer_time}")
        else:
            notification.send_notification(
                prayer_name, prayer_time, send_at
            )
            print(f"QUEUED: {prayer_name} - {prayer_time}")

    if not upcoming:
        print("No remaining prayer today.")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
