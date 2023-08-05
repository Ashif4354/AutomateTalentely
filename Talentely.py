from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from json import dump, load, loads
from os import getcwd, system, getenv, path, makedirs
from random import randint, choice, shuffle, random
from logger import logger, print_logs
from requests import get
from tkinter import Tk, Label, Button
from winsound import MessageBeep, MB_ICONHAND
from webbrowser import open_new


class AT:

    def __init__(self):
        self.version = '8.8'
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"

    def create_configuration_files(self):

        if not path.exists(self.AT_folder_path):
            makedirs(self.AT_folder_path)

        if not path.exists(path.join(self.AT_folder_path, 'TestStatus.json')):
            with open(f'{self.AT_folder_path}/TestStatus.json', 'w') as file:
                file.write('{"COMPLETED": [], "INCOMPLETE": [], "ERROR": []}')

        if not path.exists(path.join(self.AT_folder_path, 'Configuration.json')):
            with open(f'{self.AT_folder_path}/Configuration.json', 'w') as file:
                file.write('{"email": "", "password": "", "answer-percentage": 100, "time-percentage": 100, "attend-c-test": false, "version": ""}')
        
        if path.exists(path.join(self.AT_folder_path, 'Configuration.json')):
            with open(f'{self.AT_folder_path}/Configuration.json', 'r') as file:
                conf = load(file)
            conf['version'] = self.version

            with open(self.AT_folder_path + '/Configuration.json', 'w') as json_file:
                dump(conf, json_file)

    def check_update(self):
        try:
            response = get('https://tcsversion.netlify.app')
        except Exception:
            #print(1)
            return

        new_version = loads(response.text)['version']

        with open(f'{self.AT_folder_path}/Configuration.json', 'r') as file:
            old_version = load(file)['version']

        if new_version != old_version:
            MessageBeep(MB_ICONHAND)
            alert_box = Tk()
            alert_box.title("Good News")
            alert_box.geometry("300x125")
            label = Label(alert_box, text="A new version of the app is available")
            label.pack()
            label = Label(alert_box, text=f"Download v{new_version} now at ")
            label.pack()
            label = Label(alert_box, text='https://automatetalentely.netlify.app/', fg="blue", cursor="hand2")
            label.bind("<Button-1>", lambda event: open_new('https://automatetalentely.netlify.app/'))
            label.pack()            
            label = Label(alert_box, text=f"Install new version before continuing")
            label.pack()
            button = Button(alert_box, text="OK", command=alert_box.destroy)
            button.config(width=10, height=1)
            button.pack()
            alert_box.mainloop()

class Talentely:
    def __init__(self, email = '', password = 'vidhai', answer_percentage = 100, time_percentage = 100, attend_c_test = False):        
        self.url = 'https://system.talentely.com/login'
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
        self.browser  = None        
        self.current_user = getenv('USERNAME')
        self.email = email
        self.password = password
        self.tests = None
        self.incomplete_tests = None
        self.coding_tests = ('c', )
        self.answer_percentage = answer_percentage
        self.time_percentage = time_percentage
        self.attend_c_test = attend_c_test
        self.logger = logger(self.email, AT().version)

    def open_browser(self, maximize = True):
        self.browser = webdriver.Edge()
        print_logs('# browser opened')
        if maximize:
            self.browser.maximize_window()
            print_logs('# browser maximized')    

    def login(self):
        self.open_browser()
        self.browser.get(self.url)
        print_logs('# talentely login opened')

        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, 'username'))) 

        email_field = self.browser.find_element(By.ID, 'username')        
        email_field.send_keys(self.email)

        password_field = self.browser.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        
        password_field.send_keys(Keys.ENTER)

        print_logs('# login successful')

    def navigate_home_page(self, test):
        print_logs('# in navigate home page')
        try:
            academy_menu_button_xpath = '//*[@id="side-content"]/div/div/div/ul/a[6]/div'
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, academy_menu_button_xpath)))
            print_logs('# academy button appeared')
            academy_menu_button = self.browser.find_element(By.XPATH, academy_menu_button_xpath)
            print_logs('# academy menu button found')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', academy_menu_button)
            academy_menu_button.click()
            print_logs('# academy menu button clicked')
        except:
            pass
        
        try:
            if test[0] == 'a':
                aptitude_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button'
                WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, aptitude_button_xpath)))  
                print_logs('# aptitude button appeared')     
                aptitude_button = self.browser.find_element(By.XPATH, aptitude_button_xpath)
                print_logs('# aptitude button found')
                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', aptitude_button)
                

            elif test[0] == 'c' and self.attend_c_test:
                c_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/button'
                WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, c_button_xpath)))
                print_logs('# c button appeared')
                c_button = self.browser.find_element(By.XPATH, c_button_xpath)
                print_logs('# c button found')
                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', c_button)
                
            else:
                pass

            try:
                ongoing_test_cancel_button_xpath = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
                ongoing_test_cancel_button = self.browser.find_element(By.XPATH, ongoing_test_cancel_button_xpath)
                ongoing_test_cancel_button.click()
                sleep(.5)
            except:
                pass

            if test[0] == 'a':
                aptitude_button.click()
                print_logs('# aptitude button clicked')                
                self.navigate_aptitude(test)

            elif test[0] == 'c':
                c_button.click()
                print_logs('# c button clicked')                
                self.navigate_c(test)
            else:
                pass

        except Exception as exception:        
            print('\nSOME ERROR OCCURED', str(exception)[:200])
            self.logger.report_exception(test, 'Navigate_home_page', str(exception)[:200])
            input('NOTE DOWN THE ABOVE ERROR along with screenshot of the BROWSER window when the error occured and ping the developer')

        #input()

    def navigate_aptitude(self, test):
        print_logs('# in navigate aptitude')
        
        self.browser.execute_script("window.scrollTo(0, 200);")

        if test[1] == 'q':
            quantitative_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a'
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, quantitative_button_xpath)))
            print_logs('# quantitative button appeared')
            quantitative_button = self.browser.find_element(By.XPATH, quantitative_button_xpath)
            print_logs('# quantitative button found')

            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', quantitative_button)
            quantitative_button.click()
            print_logs('# quantitative button clicked')

        elif test[1] == 'r':
            reasoning_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a'
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, reasoning_button_xpath)))
            print_logs('# reasoning button appeared')
            reasoning_button = self.browser.find_element(By.XPATH, reasoning_button_xpath)
            print_logs('# reasoning button found')

            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', reasoning_button)
            reasoning_button.click()
            print_logs('# reasoning button clicked')

        elif test[1] == 'v':
            verbal_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a'
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, verbal_button_xpath)))
            print_logs('# verbal button appeared')
            verbal_button = self.browser.find_element(By.XPATH, verbal_button_xpath)
            print_logs('# verbal button found')

            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', verbal_button)
            verbal_button.click()
            print_logs('# verbal button clicked')

        else:
            pass
        
        self.find_and_do_test(test)

    def navigate_c(self, test):
        print_logs('# in navigate c')
        basic_c_button_xpath = '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a'
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, basic_c_button_xpath)))
        print_logs('# basic c button appeared')
        basic_c_button = self.browser.find_element(By.XPATH, basic_c_button_xpath)
        print_logs('# basic c button found')
        
        self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', basic_c_button)
        basic_c_button.click()
        print_logs('# basic c button clicked')

        self.find_and_do_test(test)

    def generate_test_status(self):
        print_logs('# in generate test status')
        self.tests = self.get_json('tests')['TESTS']

        test_status = self.get_json('TestStatus')
        print_logs('# fetched test status json')

        for test in self.tests:
            if not test in test_status['COMPLETED'] and test not in test_status['INCOMPLETE'] and test not in test_status['ERROR']:
                test_status['INCOMPLETE'].append(test)
        
        if not self.attend_c_test:
            inc_tests = test_status['INCOMPLETE'].copy()
            for test in inc_tests:
                if test[0] == 'c':
                    test_status['INCOMPLETE'].remove(test)

        self.incomplete_tests = test_status['INCOMPLETE']

        with open(self.AT_folder_path + '/TestStatus.json', 'w') as json_file:
            dump(test_status, json_file)
        print_logs('# test status generated')

    def update_test_status(self, test, success):
        print_logs('# in update test status')

        test_status = self.get_json('TestStatus')
        print_logs('# fetched test status json')

        if success:
            test_status['COMPLETED'].append(test)
            test_status['INCOMPLETE'].remove(test)
        else:
            test_status['ERROR'].append(test)
            test_status['INCOMPLETE'].remove(test)
        
        with open(self.AT_folder_path + '/TestStatus.json', 'w') as json_file:
            dump(test_status, json_file)
        print_logs('# test status updated')

    def perform_tests(self):
        print_logs('# IN PERFORM TESTS')
        self.generate_test_status()        

        for test in self.incomplete_tests:
            print_logs('#\n\n\n')
            print_logs('# TEST processing', test)
            self.navigate_home_page(test)
        
        for test in self.get_json('TestStatus')['ERROR']:
            print_logs('#\n\n\n')
            print_logs('# ERRORED TEST processing', test)
            self.navigate_home_page(test)

        incomplete_tests = self.get_json('TestStatus')['INCOMPLETE']
        print_logs('# incomplete tests fetched')

        if not self.attend_c_test:
            for test in incomplete_tests:
                if test[0] == 'c':
                    incomplete_tests.remove(test)

        if incomplete_tests == []:
            print('SUCCESS !!!! COMPLETED')
            print('SUCCESS !!!! COMPLETED\n\n')
            print(f"{len(self.get_json('TestStatus')['ERROR'])} tests error")        
            self.browser.close()

        input('PRESS ENTER TO CONTINUE')#This line is to keep the app window open after completion

    def get_json(self, file):
        print_logs('# in get json')
        json_ = {}
        try:
            with open(f'{self.AT_folder_path}/{file}.json', 'r') as json_file:
                json_ = load(json_file)
        except:
            try:
                with open(f'{file}.json', 'r') as json_file:
                    json_ = load(json_file)
            except:
                with open(f'{getcwd()}\jsonFiles\{file}.json', 'r') as json_file:
                    json_ = load(json_file)
        print_logs('# found json file')
        return json_

    def get_test_xpath(self, test):
        print_logs('# in get test xpath')
        if test[1] == 'q':
            return self.get_json('Qtests')[test[2]]
        elif test[1] == 'r':
            return self.get_json('Rtests')[test[2]]
        elif test[1] == 'v':
            return self.get_json('Vtests')[test[2]]
        elif test[1] == 'b':
            return self.get_json('Ctests')[test[2]]
        else:
            pass

    def get_test_time(self, test, index):
        print_logs('# in get test time')
        test_time_xpath = f'//*[@id="height{index - 1}"]/div/div/div/div[2]/p[1]/b'
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, test_time_xpath)))
        print_logs('# test time appeared')
        test_time = self.browser.find_element(By.XPATH, test_time_xpath)
        test_time = test_time.text.replace(' ', '').split(':')
        print_logs('# test time fetched')

        if len(test_time) == 2:
            hours = 0
        elif len(test_time) == 3:
            hours = int(test_time[0])
        else:
            pass

        minutes = int(test_time[-2])
        seconds = int(test_time[-1])

        total_time = (hours * 3600) + (minutes * 60) + seconds
        print_logs('# total calculated time:', total_time)        

        if total_time == 0 and test[0] == 'c':
            total_time = 5400

        elif total_time == 0 and test[0] == 'a':
            total_time = 1200
        
        print_logs('# total calculated timeafter adjustment:', total_time)
        return (total_time, test_time)

    def click_test(self, test):
        print_logs('# in click test')

        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, f'stepper1')))
        print_logs('# tests menu appeared')
        sleep(1)
        
        count = 1
        while True:
            print_logs('# stepper count ', count)
            try:
                test_button_2 = self.browser.find_element(By.ID, f'stepper{count}')
            except:
                return 'Not Found'
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button_2)
            
            print_logs('# the text in each stepper value : ' + test_button_2.text.lower())
            if test[4].lower() in test_button_2.text.lower():
                print_logs('# test found')
                test_button_2.click()
                print_logs('# test clicked')
                break
            
            count += 1
        print_logs('# returned index', count)   
        return count

    
    def find_and_do_test(self, test):
        print_logs('# in find and do test')
        test_xpath = self.get_test_xpath(test)
        
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, test_xpath)))
            print_logs('# test button appeared')
            test_button = self.browser.find_element(By.XPATH, test_xpath)
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button)
            print_logs('# test button found in try itself')
        except:
            self.browser.execute_script("window.scrollTo(0, 200);")
            test_button = self.browser.find_element(By.XPATH, test_xpath)
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button)
            print_logs('# test button found in except')

        test_button.click()
        print_logs('# test button clicked')
        #sleep(2)
        
        index = self.click_test(test)

        if index == 'Not Found':
            self.browser.back()
            self.browser.back()
            self.browser.back()
            return

        test_name = test[4]

        body = self.browser.find_element(By.XPATH, '/html/body')
        body.click()
        print_logs('# body clicked')

        test_time = self.get_test_time(test, index)
        print_logs('# got test time')

        try:
            start_test_button_xpath = f'//*[@id="height{index - 1}"]/div/div/div/button/span[1]'
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, start_test_button_xpath)))
            print_logs('# start button appeared')
            start_test_button = self.browser.find_element(By.XPATH, start_test_button_xpath)

            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', start_test_button)
            print_logs('# start button found, going to click it')
            self.start_test(start_test_button, test_name, test_time[1])

        except Exception as exception:
            print_logs('# in except, probably start button not found')
            self.update_test_status(test, False)
            #self.browser.get('https://system.talentely.com/academy/courses')
            self.browser.back()
            self.browser.back()
            self.browser.back()
            return 

        try:
            print_logs('# a test already in progress')
            submit_button_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[1]'
            WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located((By.XPATH, submit_button_xpath)))
            print_logs('# submit button appeared')
            submit_button = self.browser.find_element(By.XPATH, submit_button_xpath)
            print_logs('# submit button found')
            submit_button.click()
            print_logs('# submit button clicked')
            sleep(4)
            
            proceed_button_xpath = '/html/body/div[3]/div[3]/div/div[3]/button[2]'
            proceed_button = self.browser.find_element(By.XPATH, proceed_button_xpath)
            print_logs('# proceed button found') 
            proceed_button.click()
            print_logs('# proceed button clicked')
        except Exception as e:
            pass                 

        try:
            end_button_xpath = '//*[@id="FullScreen"]/div[2]/div/div[3]/button[6]'
            WebDriverWait(self.browser, 4).until(EC.visibility_of_element_located((By.XPATH, end_button_xpath)))
            print_logs('# end button appeared and found')
            
            try:
                print_logs('#', test_name, 'trying to get answers')
                answers = self.get_answers(test_name)
                print_logs('#', test_name, 'got answers')
            except:
                print_logs('#', test_name, 'in except coz no answers found')
                self.end_test(test, answered = False)   
            
            print_logs('#', test_name, 'going to do test')
            self.do_test(test, test_time, answers) 
            print_logs('#', test_name, 'test done, going to press end button',)           

            self.end_test(test, answered = True)
            print_logs('#', test_name, 'test_ended')

        except Exception as exception:
            print_logs('#', test_name, '\n', str(exception)[:200])
            self.logger.report_exception(test, 'find_and_do_test', str(exception)[:200])
            #print("EXCEPTION", exception)
            print_logs('# Going to endtest2')
            self.end_test2(test) 
            print_logs('# endtest2 success')      
        
    
    def start_test(self, start_button, test_name, test_time):
        start_button.click()
        self.logger.log_start_test(test_name, test_time)
    
    def get_answers(self, test_name):
        print_logs('# in get answers')
        answers = {}

        answers = self.get_json('Answers')[test_name]
        print_logs('# answers:', answers)
        
        return answers

    def get_number_of_questions(self):
        print_logs('# in get_number_of_questions')
        number = 1
        questions = 0
        
        three_line_button_xpath = '//*[@id="drawer-container"]/div[1]/button'
        three_line_button = self.browser.find_element(By.XPATH, three_line_button_xpath)
        print_logs('# three line button found')
        three_line_button.click()
        print_logs('# three line button clicked, finding number of questions')

        while True:
            try:
                self.browser.find_element(By.XPATH, f'//*[@id="drawer-container"]/div[2]/div/div[1]/div[2]/div[{number}]/button')
                
            except:
                questions = number - 1
                break
            number += 1
        print_logs('# number of questions found to be', questions)
        return questions

    def get_random_time(self, test_time, no_of_questions):
        print_logs('# in get random time')
        time_for_each_question = []
        
        print_logs('# before calculating total time, test time:', test_time, 'no of questions:', no_of_questions)
        total_calculated_time = (test_time * self.time_percentage / 100) - (no_of_questions * 2)
        print_logs('# total calculated time:', total_calculated_time)

        if total_calculated_time > test_time - 30:
            total_calculated_time = test_time - 30
        print_logs('# total calculated time after adjustment:', total_calculated_time)

        if no_of_questions % 2 == 0:
            even = True
            loop_count = no_of_questions / 2
        else:
            even = False
            loop_count = (no_of_questions // 2) + 1
        
        print_logs('# loop count before converting to int:', loop_count)
        loop_count = int(loop_count)
        print_logs('# loop count after converting to int:', loop_count)

        equal_time = total_calculated_time / no_of_questions
        print_logs('# calculated equal time:', equal_time)
        
        for i in range(loop_count):

            try:
                random_time  = randint(1, int(equal_time * (1 / 4)))
            except:
                random_time = random()

            if i < loop_count - 1:
                time_for_each_question.append(equal_time + random_time)
                time_for_each_question.append(equal_time - random_time)
            elif i == loop_count - 1 and not even:
                time_for_each_question.append(equal_time)   
            elif i == loop_count - 1 and even:
                time_for_each_question.append(equal_time + random_time)
                time_for_each_question.append(equal_time - random_time)
        
        print_logs('# time for each question before shuffling', time_for_each_question)
        shuffle(time_for_each_question)
        print_logs('# time for each question after shuffling', time_for_each_question)
        return time_for_each_question

    def do_test(self, test, test_time, answers):
        no_of_questions = self.get_number_of_questions()
        
        print_logs('# before calculating no of correct answers, no_of questions:', no_of_questions)
        correct_answers = int(no_of_questions * self.answer_percentage / 100)
        print_logs('# after calculating no of correct answers', correct_answers)
        
        print_logs('# before calculating random time for questions')
        time_for_each_question = self.get_random_time(test_time[0], no_of_questions)
        print_logs('# Random times calculated')
        
        if test[0] not in self.coding_tests:
            print_logs('# going into choose options')
            self.choose_options(no_of_questions, time_for_each_question, answers, correct_answers)
            print_logs('# all options choosed')
        else:
            print_logs('# going into type codes')
            self.type_codes(no_of_questions, time_for_each_question)
            print_logs('# all codes typed')

    def choose_options(self, no_of_questions, time_for_each_question, answers, correct_answers):
        print_logs('# in choose options')
       
        wrong_answers = []  

        for index in range(1, no_of_questions + 1):
            if answers[str(index)] == '':
                wrong_answers.append(index)
        print_logs('# Wrong answers after appending empty values', wrong_answers)        

        while len(wrong_answers) < no_of_questions - correct_answers:
            question_num = randint(1, no_of_questions)

            if question_num not in wrong_answers:
                wrong_answers.append(question_num)   
        print_logs('# wrong answers after appending random values to remaining spots') 

        for question in range(1, no_of_questions + 1):
            print_logs('# question number', question)
            sleep(time_for_each_question[question - 1])
            #sleep(1)
            answer = answers[str(question)].lower()        
                
            xpaths = [
                '//*[@id="drawer-container"]/div/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[3]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[2]/div/fieldset/div/label[{}]/span[2]/p'
            ]

            xpath_verified = False

            for xpath in xpaths:
                if not xpath_verified:
                    print_logs('# XPATH not verified')
                    pass
                else:
                    print_logs('# XPATH verified')
                    break
                
                try:
                    for i in range(1,7):
                        xpath_ = xpath.format(i)
                        try:
                            print_logs('# trying option ', i)
                            option = self.browser.find_element(By.XPATH, xpath_)
                            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', option)
                            print_logs('option xpath verified')
                            xpath_verified = True
                            print_logs('# option found in try itself, xpath verified ', i)
                        except Exception as exception:
                            print_logs('# probable warning encountered ', str(exception)[:200])
                            try:
                                warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                                warning_ok_button.click()
                                print_logs('# warning clicked')
                            except:
                                pass
                            
                            sleep(1)
                            option = self.browser.find_element(By.XPATH, xpath_)
                            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', option)
                            xpath_verified = True
                            print_logs('# option found in except, xpath verified', i)

                        text = option.text.lower()

                        print_logs("# checking option ", text)
                        if  (text in answer or answer in text or text == answer) or answer == '':
                            if question not in wrong_answers:                                
                                option.click()
                                print_logs('# correct answer clicked')
                                sleep(1)
                                break
                            else:
                                option_numbers = [1, 2, 3, 4] 
                                try:
                                    option_numbers.remove(i)
                                except:
                                    pass
                                
                                xpath_ = xpath.format(choice(option_numbers))
                                option = self.browser.find_element(By.XPATH, xpath_)
                                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', option)
                                option.click()
                                print_logs('# wrong answer clicked')
                                sleep(1)
                                break
                        else:
                            print_logs('# in else , probably answer didnt match any of the option')
                            continue

                    
                except Exception as exception:
                    print_logs('# in exception', str(exception)[:200])
                    #print('EXCEPTION 2', exception)
                    pass
                
            print_logs('# going to press next button')
            if not question == no_of_questions: 
                try:
                    next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                    print_logs('# next button found')
                    next_button.click()
                    print_logs('# next button clicked')
                    
                except:
                    print_logs('# in except , probably warning came')
                    warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                    warning_ok_button.click()
                    print_logs('# warning ok button clicked')
                    sleep(1)

                    next_button_xpath = '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]'
                    print_logs('# next button found in except')
                    next_button = self.browser.find_element(By.XPATH, next_button_xpath)
                    next_button.click()
                    print_logs('# next button in except clicked')

    def type_codes(self, no_of_questions, time_for_each_question):
        print_logs('# in type codes')
        
        for question in range(1, no_of_questions + 1):
            print('question number', question)
            sleep(time_for_each_question[question - 1])
            #typing_field_xpath = '//*[@id="editor"]/textarea'
            #typing_field = self.browser.find_element(By.XPATH, typing_field_xpath)
            #typing_field.click()
            #typing_field.send_keys('#include<stdio.h>')            

            if not question == no_of_questions: 
                try:
                    print_logs('# next button found')
                    next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                    next_button.click()
                    print_logs('# next button clicked')
                except:
                    print_logs('# in except, probably warning occured')
                    warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                    warning_ok_button.click()
                    print_logs('# warning button clicked')
                    sleep(1)
                    
                    print_logs('# next button found, in except')
                    next_button_xpath = '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]'
                    next_button = self.browser.find_element(By.XPATH, next_button_xpath)
                    next_button.click()
                    print_logs('# next button clicked')
        
    def end_test(self, test, answered):
        print_logs('# in end test')
        try:
            end_button_xpath = '//*[@id="FullScreen"]/div[2]/div/div[3]/button[6]'
            end_button = self.browser.find_element(By.XPATH, end_button_xpath)
            print_logs('# end button found in try itself')
        except:
            try:
                print_logs('# in try of except, probably warning occured')
                warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                warning_ok_button.click()
                print_logs('# warning button clicked')
            except:
                print_logs('# in except of except, going into end test 2')
                self.end_test2(test) 
                print_logs('# end test 2 completed')
                return

        end_button.click()
        print_logs('# end button clicked')

        submit_button_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[2]'
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, submit_button_xpath)))
        print_logs('# submit button appeared')
        submit_button = self.browser.find_element(By.XPATH, submit_button_xpath)
        submit_button.click()
        print_logs('# submit button clicked')
        sleep(5)
        
        try:
            cancel_button_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[2]'
            cancel_button = self.browser.find_element(By.XPATH, cancel_button_xpath)
            print_logs('# cancel button found')
            cancel_button.click()
            print_logs('# cancel button clicked')
        except:
            print_logs('# in except, probably cancel button not found, probably another button appeared')
            button_xpath = '/html/body/div[4]/div[3]/div/div[3]/button'
            button = self.browser.find_element(By.XPATH, button_xpath)
            print_logs('# another button found')
            button.click()
            print_logs('# another button clicked')

        
        if answered:
            self.update_test_status(test, True)
            self.logger.log_end_test(len(self.get_json('TestStatus')['COMPLETED']))            
        else:
            self.logger.log_no_answers()


    def end_test2(self,test):
        print_logs('# in end test 2')
        sleep(5)
        
        try:
            button_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[2]'
            button = self.browser.find_element(By.XPATH, button_xpath)
            print_logs('# some button found')
            button.click()
            print_logs('# some button clicked')
        except:
            ok_button_xpath = '/html/body/div[4]/div[3]/div/div[3]/button[1]'
            ok_button = self.browser.find_element(By.XPATH, ok_button_xpath)
            print_logs('# ok button found')
            ok_button.click()
            print_logs('# ok button clicked')

        self.logger.log_test_error(len(self.get_json('TestStatus')['COMPLETED']))
        self.update_test_status(test, False)
