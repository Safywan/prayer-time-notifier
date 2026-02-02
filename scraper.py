'''
Function that returns the prayer times from the local mosque website
'''
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
PRAYER_NAMES = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]


def fetch_prayer_times(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Open up a tab in the browser
        page = browser.new_page()
        # Navigate to the mosque website
        page.goto(url)

        # Get HTML content
        html_script = page.content()

        # Close the browser
        browser.close()

        # Use beautiful soup to parse and extract prayer times
        soup = BeautifulSoup(html_script, 'html.parser')

        prayer_times = [time.text.strip()
                        for time in soup.find_all(class_='eeeHOUR')]

        # Delete the first element as its not a prayer time
        del prayer_times[0]

        # Return the dictionary with prayer name and time
        prayers = dict(zip(PRAYER_NAMES, prayer_times))

        return prayers
