# Prayer Time Notifier

A Python tool that scrapes **live prayer times** from a local mosque website (JavaScript-rendered) and sends **automated prayer-time notifications**.

> Source (current): awqat.com.au (MGM page)

---

## Features

- Scrapes prayer times from a dynamic website using **Playwright**
- Parses the rendered HTML using **BeautifulSoup**
- Outputs prayer times as a dictionary: `{prayer_time: prayer_name}`
- Notification system using pushover on android

---

## Tech Stack

- Python 3
- Playwright (Chromium)
- BeautifulSoup4
- Pushover
- Pythonanywhere (server)

---


