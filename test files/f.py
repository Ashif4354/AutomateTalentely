from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.get("https://www.google.com")

sleep(2)
driver.refresh()

sleep(5)
