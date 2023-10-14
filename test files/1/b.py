from selenium import webdriver
from selenium.webdriver.edge.options import EdgeOptions

options = EdgeOptions()
options.add_argument('--log-level=0')

driver = webdriver.Edge(options=options)
driver.get('https://www.google.com')

# The "DevTools listening" message will not be printed
