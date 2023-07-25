import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from main import Talentely
from bs4 import BeautifulSoup
from time import sleep

tests = {}
Answers = {}

with open('new_tests.json', 'r') as json_file:
  tests = json.load(json_file)

with open('Answers.json', 'r') as json_file:
  tests = json.load(json_file)

new_tests = {'TESTS' : []}

#tests = {'TESTS' : [["a", "v", "antonyms", 1, "Antonyms_Level_1_Test 1"]]}

def main():
    t = Talentely('20cs008@kcgcollege.com', 'vidhai')
    t.login()

    reports_button = t.browser.find_element(By.XPATH, '//*[@id="side-content"]/div/div/div/ul/a[7]')
    reports_button.click()

    sleep(2)
    count_ = 0
    for test in tests['TESTS']:

        course_option_button = t.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]')
        t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', course_option_button)
        course_option_button.click()

        if test[0] == 'a':
            aptitude_option = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', aptitude_option)
            aptitude_option.click()

        elif test[0] == 'c':
            c_option = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[2]')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', c_option)
            c_option.click()



        sleep(1)
        
        select_test_button = t.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div')
        t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', select_test_button)
        select_test_button.click()
        
        count = 1
        while True:
            #print(f'count {count}')
            menu_option_xpath = f'//*[@id="menu-"]/div[3]/ul/li[{count}]'

            try:
                menu_item = t.browser.find_element(By.XPATH, menu_option_xpath)
                if menu_item.text == test[4]:
                    t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', menu_item)
                    menu_item.click()
                    break
                #print(count, option.text)
                count += 1
            except Exception as exception:
                print(f'test not found {test}')
                break
        
        try:
            select_attempt_button = t.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[1]/div[3]/div')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', select_attempt_button)
            select_attempt_button.click()

            first_attempt = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
            first_attempt.click()

            sleep(1)

            view_report_button = t.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[1]/button')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', view_report_button)
            view_report_button.click()
            sleep(2)
            
        except:
            menu_item = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', menu_item)
            menu_item.click()

            continue
        
        number = 1
        answers_ = {}
        

        if test[0] == 'a':
            while True:
                try:
                    answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                    answer = t.browser.find_element(By.XPATH, answer_xpath)
                    answers_[number] = answer.text
                    #print(answer.text)
                    number += 1
                except Exception as exception:
                    #print('in except', exception)
                    break
        elif test[0] == 'c':
            pass
        
        #print(answers_)
        Answers[test[4]] = answers_        

        with open('Answers.json', 'w') as json_file:
            json.dump(Answers, json_file)
        
        count_ += 1
        print(count_)

if __name__ == '__main__':
    main()



