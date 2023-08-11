from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def find_and_click_element_by_xpath(browser, xpath, name = ''):
    element = browser.find_element(By.XPATH, xpath)
    browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', element)
    element.click()
    print(name + ' clicked')
    sleep(2)

def find_and_click_element_by_id(browser, id, name = ''):
    element = browser.find_element(By.ID, id)
    browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', element)
    element.click()
    print(name + ' clicked')
    sleep(2)

browser = webdriver.Edge()
browser.maximize_window()

browser.get('https://system.talentely.com/login')
print('Login page fetched')
sleep(2)

email_field = browser.find_element(By.ID, 'username')        
email_field.send_keys('20cs062@kcgcollege.com')

password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys('vidhai')

password_field.send_keys(Keys.ENTER)
print('Login Success')
sleep(5)

find_and_click_element_by_xpath(browser, '//*[@id="side-content"]/div/div/div/ul/a[6]/div', 'academy button')

find_and_click_element_by_xpath(browser, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button', 'aptitude button')

aptitude_tests_xpaths = {
    'q' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'r' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'v' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a'
}

