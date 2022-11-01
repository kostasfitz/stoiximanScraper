# stoiximan scraper

import time
import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By


# scraper setup
driver_path = 'C:\Drivers\chromedriver_win32\chromedriver.exe'
website = 'https://www.stoiximan.gr/sport/tenis/kouponi-agones-simera/'
driver = webdriver.Chrome(driver_path)
driver.get(website)

# excel setup
excel_path = 'data.xlsx'

# close popups
cookies_button = driver.find_element(by=By.ID, value='onetrust-accept-btn-handler')
cookies_button.click()
popup_button = driver.find_element(by=By.XPATH, value="//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
popup_button.click()

# find available matches
time.sleep(1)
table = driver.find_element(by=By.XPATH, value="//table[@class='events-list__grid']")
rows = table.find_elements(by=By.XPATH, value="//tr[@class='events-list__grid__event']")

for row in rows:
    event = row.get_attribute('innerText')
    date, time, home, away, w, home_odds, away_odds, y = event.split('\n')
    print(date, time, home, away, home_odds, away_odds)

# for row in rows[:2]:
#     participants = row.find_elements(by=By.XPATH, value="//span[@class='events-list__grid__info__main__participants__participant-name']")
#     for participant in participants:
#         print(participant.get_attribute('innerText'))
#     # away = participants.pop()
#     # home = participants.pop()
#     # print(home.get_attribute('innerText'))
#     # print(away.get_attribute('innerText'))
#
#     #print(row.get_attribute('innerText'))
#     # x = row.find_elements(by=By.TAG_NAME, value="button")
#     # for y in x:
#     #     print(y.get_attribute('innerText'))


driver.close()
