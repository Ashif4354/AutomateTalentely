import logger
from selenium import webdriver

browser = webdriver.Edge()
browser.get('https://www.google.com')
logger.logger('20cs008@kcgcollege.com', '1.1').report_exception((1,2), 'a.py', 'hello exception', browser)