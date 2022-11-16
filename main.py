# stoiximan scraper

from tennis_scrape import tennis_scrape


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://en.stoiximan.gr/sport/tenis/diorganoseis/199527r,199528r/'

tennis_scrape(driver_path, website)
