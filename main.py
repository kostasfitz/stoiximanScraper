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
# cookies_button.click()
# popup_button = driver.find_element(by=By.XPATH, value="//button[@class='sb-modal__close__btn uk-modal-close-default uk-icon uk-close']")
# popup_button.click()

