from selenium import webdriver
from time import sleep

browser = webdriver.Edge()

browser.get('https://google.com')

sleep(1)

browser.back()

sleep(1)

browser.forward()

sleep(1)

browser.back()

sleep(1)

browser.forward()

sleep(1)

browser.back()

sleep(1)

browser.forward()