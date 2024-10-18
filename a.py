# import logger
# from selenium import webdriver

# browser = webdriver.Edge()
# browser.get('https://www.google.com')
# logger.logger('', '1.1').report_exception((1,2), 'a.py', 'hello exception', browser)

# exit()

from requests import get
from requests_html import HTMLSession

with HTMLSession() as session:
    response = session.get('https://automatetalentely.netlify.app/version')
    response.html.render()
    # response = session.render(response)
    with open('a.html', 'w') as f:
        f.write(response.text)