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
# tests = {
#     "TESTS": [
#         ['c', 'ad', 'advanced bit manipulation', 5, 'upd_adv_bit_manipulation_L2'],
#         ['c', 'ad', 'advanced arrays', 3, 'upd_Adv_1D_Array_L0'],
#         ['c', 'ad', 'advanced arrays', 4, 'upd_Adv_1D_Array_L1'],
#         ['c', 'ad', 'advanced arrays', 5, 'upd_Adv_1D_Array_L2'],
#     ]
# }



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
                print(test, len(Answers[test[4]]))
                # print(test, Answers[test[4]])
        except KeyError:
            no_answers.append(test)

        count += 1
    print(count)
    print('\n\n')
    for test in no_answers:
        print(test)

def main():
    t = Talentely('', 'vidhai')
    t.login()

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
            c_option = t.browser.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[3]')
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
            actions = ActionChains(t.browser)
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
        
        number = 1 # change to 1
        answers_ = {}
        
        not_found_count = 0
        
        if test[0] == 'a':
            print(test)
            
            
            while True:
                xpaths = [
                    f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p',
                    f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p',
                    f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[2]/div[2]/p',
                    f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                ]
                
                try:
                    # try:              #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/p'
                    #     answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                    #     answer = t.browser.find_element(By.XPATH, answer_xpath)
                    # except:           #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/p
                    #     try:          #f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[2]/div[2]/p
                    #         answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[7]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                    #         answer = t.browser.find_element(By.XPATH, answer_xpath)
                    #     except:
                    #         try:
                    #             answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[2]/div[2]/p'
                    #             answer = t.browser.find_element(By.XPATH, answer_xpath)
                    #         except:
                    #             try:
                    #                 answer_xpath = f'//*[@id="main-content"]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/p'
                    #                 answer = t.browser.find_element(By.XPATH, answer_xpath)
                    #             except:
                    #                 raise Exception

                    for xpath in xpaths:
                        try:
                            answer = t.browser.find_element(By.XPATH, xpath)
                            break
                        except:
                            continue

                    else:
                        raise Exception
                                
                        
                    answers_[number] = answer.text
                    #print(answer.text)
                    number += 1
                    not_found_count = 0

                except Exception as exception:                    
                    print('in except of a test', exception)
                    if not_found_count == 5:
                        break
                    else:
                        answers_[number] = ''
                        number += 1
                        not_found_count += 1
                        continue
                    
        elif test[0] == 'c':
            print(test)

            while True:

                xpaths = [
                    f'/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/div/div[2]/div',
                    f'/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[8]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div[1]/div[3]/div[2]/div/div[2]/div',
                    f'/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[{number}]/td/div/div/div/div[2]/div[2]/div/div[2]/div'
                ]     

                try:
                    for xpath in xpaths:
                        try:
                            # code_lines = [ x for x in t.browser.find_element(By.XPATH, xpath).text.split('\n')]
                            # # answer = [ x.replace('""', '"') for x in answer if 'printf' in x or 'scanf' in x]
                            # # print('code lines: ', code_lines)
                            # answer = []

                            # for i in range(len(code_lines)):
                            #     if 'printf(' in code_lines[i] or 'scanf(' in code_lines[i]:
                            #         code_lines[i] = code_lines[i].replace('""', '"')
                            #         # answer += code_lines[i] + '\n'
                            #         answer.append(code_lines[i])
                            #     else:
                            #         # answer += code_lines[i] + '\n'
                            #         answer.append(code_lines[i])

                            # sleep(2)

                            t.browser.find_element(By.XPATH, xpath).click()

                            ActionChains(t.browser).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
                            sleep(.5)
                            ActionChains(t.browser).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

                            selected_text = t.browser.execute_script("return navigator.clipboard.readText()")                            
                            # selected_text = t.browser.execute_script("return document.execCommand('paste')")

                            # print('selected text: \n')
                            # print(selected_text.split('\n'))
                            # print('text printed')

                            answer = selected_text
                            
                            break
                        except Exception as exception:
                            # print('exception', number, exception)
                            continue
                    else:
                        # print('in raise exception else')
                        raise Exception
                    
                    answers_[number] = answer
                    print(answers_)
                    # raise Exception # remove this

                    number += 1
                    not_found_count = 0

                except Exception as exception:
                    print('in except of c test', exception)
                    if not_found_count == 5:
                        break
                    else:
                        answers_[number] = ''
                        number += 1
                        not_found_count += 1
                        continue
        print('going to print answers_')
        print(answers_)

        Answers[test[4]] = answers_        

        with open('Answers.json', 'w') as json_file:
            # pass
            json.dump(Answers, json_file)
        
        count_ += 1
        print(count_)

def edit_answers_json():
    with open('Answers.json', 'r') as json_file:
        with open('Answers2.json', 'w') as json_file2:
            json.dump(json.load(json_file), json_file2, indent=4)

def check_programming_answers():
    with open('Answers.json', 'r') as json_file:
        Answers = json.load(json_file)

    with open('tests.json', 'r') as json_file:
        tests = json.load(json_file)
    
    # for test in tests['TESTS']:
    #     if test[4] not in Answers:
    #         print(test[4])

    for test in tests['TESTS']:
        # print('else', test[4])
        try:
            if len(Answers[test[4]]) < 6:
                print(test[4], len(Answers[test[4]]))
        except KeyError:
            pass

def check_test_answer():
    with open('Answers.json', 'r') as json_file:
        Answers = json.load(json_file)
        count = 0
        for test in Answers:
            if Answers[test]['1'] == Answers[test]['2'] == Answers[test]['3'] == Answers[test]['4'] == Answers[test]['5'] == Answers[test]['6'] == Answers[test]['7'] == Answers[test]['8'] == Answers[test]['9'] == Answers[test]['10']:
                print(test)
                count += 1
            else:
                # print(count)
                count += 1
        # print(1, len(Answers))

def change_answer():
    with open('Answers.json', 'r') as json_file:
        Answers = json.load(json_file)
    
    Answers['upd_bt_level_0']['2'] = ''
    Answers['upd_bt_level_0']['3'] = ''
    Answers['upd_bt_level_0']['4'] = ''
    Answers['upd_bt_level_0']['5'] = ''
    Answers['upd_bt_level_0']['6'] = ''

    del Answers['upd_bt_level_0']['7']
    del Answers['upd_bt_level_0']['8']
    del Answers['upd_bt_level_0']['9']
    del Answers['upd_bt_level_0']['10']
    del Answers['upd_bt_level_0']['11']
    del Answers['upd_bt_level_0']['12']
    del Answers['upd_bt_level_0']['13']
    del Answers['upd_bt_level_0']['14']
    del Answers['upd_bt_level_0']['15']

    with open('Answers.json', 'w') as json_file:
        json.dump(Answers, json_file)

if __name__ == '__main__':
    try:
        # main()
        check_answers()
        # edit_answers_json()
        # check_programming_answers()
        # check_test_answer()
        # change_answer()
# 
    except Exception as exception:
        print('in exception')
        print(exception)
        input()
        input()


# '/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div[3]/div[1]'
# '/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div[3]/div[3]'
# '/html/body/div[1]/div[1]/div/main/div/div/div[2]/div/div/div[2]/div/div/div[9]/div/div/div/div/table/tbody/tr[1]/td/div/div/div[1]/div[3]/div[2]/div/div[2]/div/div[3]/div[1]'

