import json
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# from bs4 import BeautifulSoup
from time import sleep

from os import getcwd, environ
from sys import path
path.append(getcwd().rstrip('other py'))
from Talentely import Talentely


tests = {}
with open('tests.json', 'r') as json_file:
    tests = json.load(json_file)
tests = {
    "TESTS": [
        ["a", "r", "direction sense", 2, "Direction Sense_Level_1_Test 2"], 
        ["a", "v", "sentence correction", 2, "sentence correction_level 1_test 1"]
    ]
}



Answers = {}
with open('Answers.json', 'r') as json_file:
    Answers = json.load(json_file)
environ['print-logs'] = 'FALSE'


def check_answers():
    no_answers = []
    count = 0
    for test in tests['TESTS']:
        # print(test)
        try:
            if len(Answers[test[4]]) < 6:
                print(test)
                # print(test, Answers[test[4]])
        except KeyError:
            no_answers.append(test)

        count += 1
    print(count)
    print('\n\n')
    for test in no_answers:
        print(test)

def main():
    t = Talentely('20cs043@kcgcollege.com', 'vidhai')
    t.login()

    actions = ActionChains(t.browser)

    reports_button = t.browser.find_element(By.XPATH, '//*[@id="side-content"]/div/div/div/ul/a[7]')
    reports_button.click()
    
    count_ = 0
    for test in tests['TESTS']:
        sleep(1)

        course_option_button = t.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]')
        t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', course_option_button)
        course_option_button.click()
        sleep(1)

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

        sleep(1)
        
        count = 1
        found = False
        while True:
            #print(f'count {count}')
            menu_option_xpath = f'//*[@id="menu-"]/div[3]/ul/li[{count}]'

            try:
                menu_item = t.browser.find_element(By.XPATH, menu_option_xpath)
                if menu_item.text == test[4]:
                    t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', menu_item)
                    menu_item.click()
                    found = True
                    break
                #print(count, option.text)
                count += 1
            except Exception as exception:
                print(f'TEST NOT FOUND {test}')
                found = False
                break
        
        if not found:
            actions.send_keys(Keys.ESCAPE).perform()
            continue
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
            sleep(3)
            
        except:
            menu_item = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[1]')
            t.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', menu_item)
            menu_item.click()

            continue
        
        number = 1
        answers_ = {}
        
        not_found_count = 0
        xpaths = []
        if test[0] == 'a':
            print(test)
            while True:
                try:
                    try:              #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/p'
                        answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                        answer = t.browser.find_element(By.XPATH, answer_xpath)
                    except:           #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/p
                        try:          #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[2]/div[2]/p
                            answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                            answer = t.browser.find_element(By.XPATH, answer_xpath)
                        except:
                            try:
                                answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[2]/div[2]/p'
                                answer = t.browser.find_element(By.XPATH, answer_xpath)
                            except:
                                try:
                                    answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                                    answer = t.browser.find_element(By.XPATH, answer_xpath)
                                except:
                                    raise Exception
                                
                        
                    answers_[number] = answer.text
                    #print(answer.text)
                    number += 1
                    not_found_count = 0

                except Exception as exception:                    
                    print('in except', exception)
                    if not_found_count == 5:
                        break
                    else:
                        answers_[number] = ''
                        number += 1
                        not_found_count += 1
                        continue
                    
        elif test[0] == 'c':
            pass
        
        print(answers_)
        Answers[test[4]] = answers_        

        with open('Answers.json', 'w') as json_file:
            # pass
            json.dump(Answers, json_file)
        
        count_ += 1
        print(count_)

if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(exception)
        input()
        input()
    # check_answers()




