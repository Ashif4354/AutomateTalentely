from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, perf_counter
from json import load, dump

from create_json import data_Q, data_R, data_V

count = 0

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

def add_test_to_test_json(test):
    global count
    print('TOTAL TESTS FOUND : ', count)

    with open('AllTests.json', 'r') as file:
        test_ = load(file)

    if test not in test_['TESTS']:
        test_['TESTS'].append(test)
        print('TOTAL TESTS ADDED : ', len(test_['TESTS']))
        

    with open('AllTests.json', 'w') as file:
        dump(test_, file)

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

start = perf_counter()
for apt in aptitude_tests_xpaths:
    

    apt_btn_xpath = aptitude_tests_xpaths[apt]
    find_and_click_element_by_xpath(browser, apt_btn_xpath, apt + ' button')

    if apt == 'q':
        tests = data_Q
    elif apt == 'r':
        tests = data_R
    elif apt == 'v':
        tests = data_V

    for tests_ in tests:
        tests_xpath = tests[tests_]

        find_and_click_element_by_xpath(browser, tests_xpath, tests_ + ' button')
        sleep(1)

        index = 1

        while True:
            try:
                find_and_click_element_by_id(browser, f'stepper{index}', f'test at index {index}')
            except:
                print(f'Unable to click test at index {index}')
                break

            try:
                browser.find_element(By.XPATH, f'//*[@id="height{index - 1}"]/div/div/div/button/span[1]')
                count += 1
            except:
                index += 1
                continue
            
            test_name = browser.find_element(By.XPATH, f'//*[@id="stepper{index}"]/span/span[2]/span').text
            Test = ['a', apt, tests_.lower(), index, test_name]
            print(Test)
            add_test_to_test_json(Test)

            index += 1


        browser.back()
        print('Back button clicked to go to test list')
        sleep(3)

    
    browser.back()
    print('Back button clicked to go to q r v')
    sleep(3)

print(f'\n\nTIME TAKEN : {perf_counter() - start}')


#//*[@id="stepper1"]/span/span[2]/span
#//*[@id="stepper2"]/span/span[2]/span



# total test found in attempt 1 : 227
# total test found in attempt 2 : 227
# total test found in attempt 3 : 227

    

