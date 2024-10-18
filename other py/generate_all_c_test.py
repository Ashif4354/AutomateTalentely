from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, perf_counter
from json import load, dump

from create_json import data_C_b, data_C_al, data_C_d, data_C_ad

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

    with open('Alltests.json', 'r') as file:
        test_ = load(file)

    if test not in test_['TESTS']:
        test_['TESTS'].append(test)
        print('TOTAL TESTS ADDED : ', len(test_['TESTS']))
        

    with open('Alltests.json', 'w') as file:
        dump(test_, file, indent = 4)

browser = webdriver.Edge()
browser.maximize_window()

browser.get('https://system.talentely.com/login')
print('Login page fetched')
sleep(2)

email_field = browser.find_element(By.ID, 'username')        
email_field.send_keys('')

password_field = browser.find_element(By.NAME, 'password')
password_field.send_keys('vidhai')

password_field.send_keys(Keys.ENTER)
print('Login Success')
sleep(15)

find_and_click_element_by_xpath(browser, '/html/body/div[2]/div[3]/div/div[1]/button', 'some x button')

find_and_click_element_by_xpath(browser, '//*[@id="side-content"]/div/div/div/ul/a[6]/div', 'academy button')

find_and_click_element_by_xpath(browser, '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/button', 'c programming button')

tests_xpaths = {
    'b' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'ad' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'd' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'al' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a'
}

start = perf_counter()
for inner_test in tests_xpaths:
    

    inner_test_btn_xpath = tests_xpaths[inner_test]
    find_and_click_element_by_xpath(browser, inner_test_btn_xpath, inner_test + ' button')

    if inner_test == 'b':
        tests = data_C_b
    elif inner_test == 'ad':
        tests = data_C_ad
    elif inner_test == 'd':
        tests = data_C_d
    elif inner_test == 'al':
        tests = data_C_al
    

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
            Test = ['c', inner_test, tests_.lower(), index, test_name]
            print(Test)
            add_test_to_test_json(Test)

            index += 1


        browser.back()
        print('Back button clicked to go to test list')
        sleep(3)

    
    browser.back()
    print('Back button clicked to go to b ad d al')
    sleep(3)

print(f'\n\nTIME TAKEN : {perf_counter() - start}')


#//*[@id="stepper1"]/span/span[2]/span
#//*[@id="stepper2"]/span/span[2]/span


# total test found in attempt 1 : 82 (656 sec)
# total test found in attempt 1 : 82 (658 sec)
# total test found in attempt 1 : 82 (657 sec)


