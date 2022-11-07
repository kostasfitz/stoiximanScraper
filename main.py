# stoiximan scraper

from tennis_scrape import tennis_scrape


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://en.stoiximan.gr/sport/tennis/leagues/189086r/'

tennis_scrape(driver_path, website)
