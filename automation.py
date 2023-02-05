
import openpyxl
from openpyxl import *
import re
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path =r"C:\Program Files (x86)\chromedriver.exe"

driver= webdriver.Chrome(path)
driver.get("https://www.google.com/search?q=imdb&rlz=1C1CHZN_enIN1025IN1025&oq=imdb&aqs=chrome..69i57j0i433i512l2j46i433i512j0i131i433j0i433i512j69i60l2.1773j0j7&sourceid=chrome&ie=UTF-8")
driver.maximize_window()
print(driver.title)
time.sleep(5)
print("windows maximixed")

list=driver.find_element(By.CLASS_NAME, "l")
list.click()


import script


time.sleep(5)

driver.back()


shows=driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/table/tbody/tr[3]/td/div/h3/a')
shows.click()

time.sleep(5)
driver.quit()




