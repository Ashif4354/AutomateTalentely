from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, perf_counter
from json import dump, load, loads
from os import listdir, getcwd, path, system, getenv, makedirs
from datetime import datetime
from requests import get
from random import randint, choice, shuffle
from tkinter import Tk, Label, Button
from winsound import MessageBeep, MB_ICONHAND
from webbrowser import open_new

from logger import logger

class AT:

    def __init__(self):
        self.version = '7.9.1'
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"

    def create_cofiguration_files(self):

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
            return

        new_version = loads(response.text)['version']

        with open(f'{self.AT_folder_path}/Configuration.json', 'r') as file:
            old_version = load(file)['version']

        if new_version != old_version:
            MessageBeep(MB_ICONHAND)
            alert_box = Tk()
            alert_box.title("Good News")
            alert_box.geometry("300x100")
            label = Label(alert_box, text="A new version of the app is available")
            label.pack()
            label = Label(alert_box, text=f"Download v{new_version} now at ")
            label.pack()
            label = Label(alert_box, text='https://automatetalentely.netlify.app/', fg="blue", cursor="hand2")
            label.bind("<Button-1>", lambda event: open_new('https://automatetalentely.netlify.app/'))
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
        self.logger = logger(self.email)

    def open_browser(self, maximize = True):
        self.browser = webdriver.Edge()
        if maximize:
            self.browser.maximize_window()    

    def login(self):
        self.open_browser()
        self.browser.get(self.url)
        sleep(1.5)

        email_field = self.browser.find_element(By.ID, 'username')        
        email_field.send_keys(self.email)

        password_field = self.browser.find_element(By.NAME, 'password')
        password_field.send_keys(self.password)
        sleep(.5)
        password_field.send_keys(Keys.ENTER)
        
        sleep(5)

    def generate_test_status(self):
        self.tests = self.get_json('tests')['TESTS']

        test_status = self.get_json('TestStatus')

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

    def update_test_status(self, test, success):
        test_status = self.get_json('TestStatus')
        if success:
            test_status['COMPLETED'].append(test)
            test_status['INCOMPLETE'].remove(test)
        else:
            test_status['ERROR'].append(test)
            test_status['INCOMPLETE'].remove(test)
        
        with open(self.AT_folder_path + '/TestStatus.json', 'w') as json_file:
            dump(test_status, json_file)

    def perform_tests(self):
        self.generate_test_status()        

        for test in self.incomplete_tests:
            self.navigate_home_page(test)

        incomplete_tests = self.get_json('TestStatus')['INCOMPLETE']

        if not self.attend_c_test:
            for test in incomplete_tests:
                if test[0] == 'c':
                    incomplete_tests.remove(test)

        if incomplete_tests == []:
            print('SUCCESS !!!! COMPLETED')
            print('SUCCESS !!!! COMPLETED\n\n')
            print(f"{len(self.get_json('TestStatus')['ERROR'])} tests error")        
            self.browser.close()

        input('PRESS ENTER')#This line is to keep the app window open after completion
        

    def navigate_home_page(self, test):

        self.browser.execute_script("window.scrollTo(0, 200);")

        try:
            if test[0] == 'a':
                aptitude_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button')
                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', aptitude_button)
                aptitude_button.click()
                sleep(2)
                self.navigate_aptitude(test)

            elif test[0] == 'c' and self.attend_c_test:
                c_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/button')
                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', c_button)
                c_button.click()
                sleep(2)
                self.navigate_c(test)
                
            else:
                pass
        except Exception as exception:#log needed        
            print('\nSOME ERROR OCCURED', exception)
            self.logger.report_exception(test, 'Navigate_home_page', exception)
            input('NOTE DOWN THE ABOVE ERROR and ping DG')
            
            
    
    def navigate_aptitude(self, test):
        
        self.browser.execute_script("window.scrollTo(0, 200);")

        if test[1] == 'q':
            quantitative_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', quantitative_button)
            quantitative_button.click()
            sleep(2)

        elif test[1] == 'r':
            reasoning_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', reasoning_button)
            reasoning_button.click()
            sleep(2)

        elif test[1] == 'v':
            verbal_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', verbal_button)
            verbal_button.click()
            sleep(2)

        else:
            pass
        
        self.find_and_do_test(test)

    def navigate_c(self, test):
        basic_c_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
        self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', basic_c_button)
        basic_c_button.click()
        sleep(2)

        self.find_and_do_test(test)

    
    def get_json(self, file):
        json_ = {}
        try:
            with open(f'{self.AT_folder_path}/{file}.json', 'r') as json_file:
                json_ = load(json_file)
        except:
            with open(f'{file}.json', 'r') as json_file:
                json_ = load(json_file)

        return json_

    def get_test_xpath(self, test):
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
        test_time = self.browser.find_element(By.XPATH, f'//*[@id="height{index - 1}"]/div/div/div/div[2]/p[1]/b')
        test_time = test_time.text.replace(' ', '').split(':')

        if len(test_time) == 2:
            hours = 0
        elif len(test_time) == 3:
            hours = int(test_time[0])
        else:
            pass

        minutes = int(test_time[-2])
        seconds = int(test_time[-1])

        total_time = (hours * 3600) + (minutes * 60) + seconds
        

        if total_time == 0 and test[0] == 'c':
            total_time = 5400

        elif total_time == 0 and test[0] == 'a':
            total_time = 1200
     
        return (total_time, test_time)

    def click_test(self, test):
        
        count = 1
        while True:
            test_button_2 = self.browser.find_element(By.ID, f'stepper{count}')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button_2)

            if test[4].lower() in test_button_2.text.lower():
                test_button_2.click()
                break
            
            count += 1
            
        return count

    
    def find_and_do_test(self, test):
        test_xpath = self.get_test_xpath(test)
        
        try:
            test_button = self.browser.find_element(By.XPATH, test_xpath)
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button)
        except:
            self.browser.execute_script("window.scrollTo(0, 200);")
            test_button = self.browser.find_element(By.XPATH, test_xpath)
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button)

        test_button.click()
        sleep(2)

        index = self.click_test(test)

        test_name = test[4]

        body = self.browser.find_element(By.XPATH, '/html/body')
        body.click()
        sleep(1)

        test_time = self.get_test_time(test, index)

        try:
            start_test_button = self.browser.find_element(By.XPATH, f'//*[@id="height{index - 1}"]/div/div/div/button/span[1]')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', start_test_button)
            self.start_test(start_test_button, test_name, test_time[1])

        except Exception as exception:
            self.update_test_status(test, False)
            self.browser.get('https://system.talentely.com/academy/courses')
            sleep(3)
            return 

        try:
            submit_button = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[1]')
            submit_button.click()
            sleep(1)

            proceed_button = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[3]/button[2]') 
            proceed_button.click()
            sleep(5)
        except Exception as e:
            pass                 

        try:
            end_test_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[6]')
            
            try:
                answers = self.get_answers(test_name)
            except:
                self.end_test(test, answered = False)
   
            
            self.do_test(test, test_time, answers)
            

            self.end_test(test, answered = True)

        except Exception as exception: #log needed
            self.logger.report_exception(test, 'find_and_do_test', exception)
            #print("EXCEPTION", exception)
            self.end_test2(test)       
        
    
    def start_test(self, start_button, test_name, test_time):
        start_button.click()
        self.logger.log_start_test(test_name, test_time)

        sleep(5)
    
    def get_answers(self, test_name):
        answers = {}

        with open('Answers.json', 'r') as json_file:
            answers = load(json_file)[test_name]
        
        return answers

    def get_number_of_questions(self):
        number = 1
        questions = 0

        three_line_button = self.browser.find_element(By.XPATH, '//*[@id="drawer-container"]/div[1]/button')
        three_line_button.click()

        while True:
            try:
                self.browser.find_element(By.XPATH, f'//*[@id="drawer-container"]/div[2]/div/div[1]/div[2]/div[{number}]/button')
                
            except:
                questions = number - 1
                break
            number += 1
        sleep(.5)
        #x_button = self.browser.find_element(By.XPATH, '//*[@id="drawer-container"]/div[2]/div/div[1]/div[1]/button')
        #x_button.click()
        return questions

    def get_random_time(self, test_time, no_of_questions):
        time_for_each_question = []

        total_calculated_time = (test_time * self.time_percentage / 100) - (no_of_questions)

        if total_calculated_time > test_time - 30:
            total_calculated_time = test_time - 30

        if no_of_questions % 2 == 0:
            even = True
            loop_count = no_of_questions / 2
        else:
            even = False
            loop_count = (no_of_questions // 2) + 1

        loop_count = int(loop_count)

        equal_time = total_calculated_time / no_of_questions
        
        for i in range(loop_count):

            random_time  = randint(1, int(equal_time * (1 / 4)))

            if i < loop_count - 1:
                time_for_each_question.append(equal_time + random_time)
                time_for_each_question.append(equal_time - random_time)
            if i == loop_count - 1 and not even:
                time_for_each_question.append(equal_time)   
            if i == loop_count - 1 and even:
                time_for_each_question.append(equal_time + random_time)
                time_for_each_question.append(equal_time - random_time)
        
        shuffle(time_for_each_question)
        return time_for_each_question

    def do_test(self, test, test_time, answers):
        no_of_questions = self.get_number_of_questions()
        
        correct_answers = int(no_of_questions * self.answer_percentage / 100)

        time_for_each_question = self.get_random_time(test_time[0], no_of_questions)
        
        if test[0] not in self.coding_tests:
            self.choose_options(no_of_questions, time_for_each_question, answers, correct_answers)
        else:
            self.type_codes(no_of_questions, time_for_each_question)

    def choose_options(self, no_of_questions, time_for_each_question, answers, correct_answers):
       
        wrong_answers = []  

        for index in range(1, no_of_questions + 1):
            if answers[str(index)] == '':
                wrong_answers.append(index)

        while len(wrong_answers) < no_of_questions - correct_answers:
            question_num = randint(1, no_of_questions)

            if question_num not in wrong_answers:
                wrong_answers.append(question_num)    

        for question in range(1, no_of_questions + 1):
            sleep(time_for_each_question[question - 1])
            #sleep(2)
            #start = perf_counter()
            answer = answers[str(question)].lower()        
                
            xpaths = [
                '//*[@id="drawer-container"]/div/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[3]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[2]/div/fieldset/div/label[{}]/span[2]/p'
            ]

            for xpath in xpaths:
                
                try:
                    for i in range(1,7):
                        xpath_ = xpath.format(i)
                        option = self.browser.find_element(By.XPATH, xpath_)
                        self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', option)
                        text = option.text.lower()
                        if  (text in answer or answer in text or text == answer) or answer == '':
                            if question not in wrong_answers:
                                option.click()
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
                                break
                        else:
                            continue

                    
                except Exception as exception:
                    #print('EXCEPTION 2', exception)
                    pass
                
            
                        

            try:
                next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                next_button.click()
            except:
                warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                warning_ok_button.click()
                sleep(.5)

                next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                next_button.click()

    def type_codes(self, no_of_questions, time_for_each_question):
        
        for question in range(1, no_of_questions + 1):
            sleep(time_for_each_question[question - 1])
            #typing_field_xpath = '//*[@id="editor"]/textarea'
            #typing_field = self.browser.find_element(By.XPATH, typing_field_xpath)
            #typing_field.click()
            #typing_field.send_keys('#include<stdio.h>')            

            next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')

            next_button.click()
        
    def end_test(self, test, answered):
        sleep(3)
        try:
            end_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[6]')
        except:
            self.end_test2(test) 

        end_button.click()
        sleep(1)        

        submit_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        submit_button.click()
        sleep(2)

        cancel_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        cancel_button.click()
        sleep(1)

        if answered:
            self.update_test_status(test, True)
            self.logger.log_end_test(len(self.get_json('TestStatus')['COMPLETED']))            
        else:
            self.logger.log_no_answers()


    def end_test2(self,test):
        sleep(3)
        
        try:
            button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
            button.click()
        except:
            ok_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[1]')
            ok_button.click()
        sleep(1)

        self.logger.log_test_error(len(self.get_json('TestStatus')['COMPLETED']))
        self.update_test_status(test, False)

def main():  

    def reset_status():
        test_status = {
            'COMPLETED' : [],
            'INCOMPLETE' : [],
            'ERROR' : []
        }
        with open(AT_folder_path + '/TestStatus.json', 'w') as json_file:
            dump(test_status, json_file)  

    print('\nDEVELOPED BY The DG')
    print("COMPULSORILY READ THE '_README.txt' file present in the installation directory, before using this application for ease of access" )
    print('\nvisit automatetalentely.netlify.app for more..')

    with open(AT_folder_path + '/Configuration.json', 'r') as file:
            configuration = load(file)

    c_test_attend_status = 'ON' if configuration['attend-c-test'] else 'OFF'

    option = input("\n1. Start / Resume test\n2. Reset test progress\n3. Change user (test progress will be reset)\n4. Set Correct answer percentage\n5. Set Completion time percentage\n6. Toggle On/Off to Attend c programming test(without answers)(currently {})\n7. Manually select which tests to attend\n8. Show test status\n\nYOUR OPTION : ".format(c_test_attend_status))
    
    if option == '1':
        if configuration['email'] == '':
            for i in range(3):
                email = input('Email : ')
                if email[-15:] != '@kcgcollege.com':
                    print('\nEnter a valid email')
                    continue
                else:
                    configuration['email'] = email
                    break
            else:
                return
            pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
            if pwd == '':
                pwd = 'vidhai'

            configuration['password'] = pwd

            with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
                dump(configuration, json_file)

            

        t = Talentely(configuration['email'], configuration['password'], configuration['answer-percentage'], configuration['time-percentage'], configuration['attend-c-test'])       
        try:
            t.login()
        except Exception as exception: #log needed
            self.logger.report_exception(test, 'main', exception)
            print('\nSome Error Occured at login')

        print('\nAutomation Started\n')
        t.perform_tests()
    
    elif option == '2':
        reset_status()
        system('cls')
        print('\n((TEST PROGRESS HAS BEEN RESET))')
        
    elif  option == '3':
        for i in range(3):
            email = input('Email : ')
            if email[-15:] != '@kcgcollege.com':
                print('\nEnter a valid email')
                continue
            else:
                configuration['email'] = email
                break
        else:
            return
        pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
        if pwd == '':
            pwd = 'vidhai'
        configuration['password'] = pwd
        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        reset_status()
        system('cls')
        print('\n((STUDENT DETAILS HAS BEEN UPDATED and progress has been reset))')
    
    elif option == '4':

        try:
            percentage = int(input('Enter approximate percentage of questions you want to be answered correctly for all tests (The default is 100): '))

            if percentage in range(101):
                pass
            else:
                print('Percentage should be from 0 - 100')
                
                return
        except:
            print('Enter valid Percentage')
            return

        configuration['answer-percentage'] = percentage

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        system('cls')
        print('\n((ANSWER PERCENTAGE UPDATED))')
    
    elif option == '5':

        try:
            percentage = int(input('Enter approximate percentage of time you want the application to attend all tests (The default is 100): '))

            if percentage in range(101):
                pass
            else:
                print('Percentage should be from 0 - 100')
                
                return
        except:
            print('Enter valid Percentage')
            return

        configuration['time-percentage'] = percentage

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)

        system('cls')
        print('\n((TIME PERCENTAGE UPDATED))')

    elif option == '6':        
        configuration['attend-c-test'] = True if not configuration['attend-c-test'] else False

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        system('cls')
            
    elif option == '7':
        browser = webdriver.Edge()
        browser.get(path.join(getcwd(), 'select_tests.html'))
        input()
    
    elif option == '8':
        with open(AT_folder_path + '/TestStatus.json', 'r') as file:
            TestStatus = load(file)

        system('cls')
        print('Tests Completed : {}\nTests Remaining : {}\nTests Error : {}'.format(len(TestStatus['COMPLETED']), len(TestStatus['INCOMPLETE']), len(TestStatus['ERROR']), ))

    else:
        print('ENTER VALID OPTION')

if __name__ == '__main__':

    AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
    at = AT()
    at.create_cofiguration_files()
    at.check_update()

    while True:
        main()
        

    