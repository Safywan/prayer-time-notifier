import scraper

url = "https://awqat.com.au/mgm/"

def main():
    prayer_times = scraper.fetch_prayer_times(url)
    print(prayer_times)
    

if __name__ == "__main__":
    main()    