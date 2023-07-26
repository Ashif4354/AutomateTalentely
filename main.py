from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
from os import listdir
from datetime import datetime
from requests import post
from random import randint, choice

from logger import logger


class Talentely:
    def __init__(self, email, password = 'vidhai', answer_percentage = 100, time_percentage = 100, attend_c_test = False):
        self.url = 'https://system.talentely.com/login'
        self.browser  = None
        self.email = email
        self.password = password
        self.tests = None
        self.incomplete_tests = None
        self.logger = logger(self.email)
        self.coding_tests = ('c', )
        self.answer_percentage = answer_percentage
        self.time_percentage = time_percentage
        self.attend_c_test = attend_c_test
        
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

        self.incomplete_tests = test_status['INCOMPLETE']

        with open('TestStatus.json', 'w') as json_file:
            json.dump(test_status, json_file)

    def update_test_status(self, test, success):
        test_status = self.get_json('TestStatus')
        if success:
            test_status['COMPLETED'].append(test)
            test_status['INCOMPLETE'].remove(test)
        else:
            test_status['ERROR'].append(test)
            test_status['INCOMPLETE'].remove(test)
        
        with open('TestStatus.json', 'w') as json_file:
            json.dump(test_status, json_file)

    def perform_tests(self):
        self.generate_test_status()        

        for test in self.incomplete_tests:
            self.navigate_home_page(test)

        incomplete_tests = self.get_json('TestStatus')['INCOMPLETE']
        if incomplete_tests == []:
            print('SUCCESS !!!! COMPLETED')
            print('SUCCESS !!!! COMPLETED\n\n')
            print(f"{len(self.get_json('TestStatus')['ERROR'])} tests error")        
            self.browser.close()

        input('PRESS ENTER')#This line is to keep the app window open after completion
        

    def navigate_home_page(self, test):
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
        except Exception as exception:
            print('\nSOME ERROR OCCURED', exception)
            
    
    def navigate_aptitude(self, test):
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
        with open(f'{file}.json', 'r') as json_file:
            json_ = json.load(json_file)
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
        
        total_time = total_time * self.time_percentage / 100
     
        return (total_time, test_time)

    def click_test(self, test):
        
        count = 1
        while True:
            test_button_2 = self.browser.find_element(By.ID, f'stepper{count}')
            if test[4].lower() in test_button_2.text.lower():
                test_button_2.click()
                break
            
            count += 1
            
        return count

    
    def find_and_do_test(self, test):

        test_xpath = self.get_test_xpath(test)
        
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
                self.end_test(test, end_test_button, test_time[0], answered = False)
   
            
            self.do_test(test, test_time, answers)
            

            self.end_test(test, test_time[0], answered = True)

        except Exception as exception:
            self.end_test2(test)       
        
    
    def start_test(self, start_button, test_name, test_time):
        start_button.click()
        self.logger.log_start_test(test_name, test_time)

        sleep(5)
    
    def get_answers(self, test_name):
        answers = {}

        with open('Answers.json', 'r') as json_file:
            answers = json.load(json_file)[test_name]
        
        return answers

    def get_number_of_questions(self):
        number = 1
        questions = 0

        three_line_button = self.browser.find_element(By.XPATH, '//*[@id="drawer-container"]/div[1]/button')
        three_line_button.click()

        while True:
            try:
                self.browser.find_element(By.XPATH, f'//*[@id="drawer-container"]/div[2]/div/div[1]/div[2]/div[{number}]/button')
                #print(number)
            except:
                questions = number - 1
                break
            number += 1

        return questions

    def do_test(self, test, test_time, answers):
        no_of_questions = self.get_number_of_questions()
        
        correct_answers = int(no_of_questions * self.answer_percentage / 100)
        
        if test[0] not in self.coding_tests:
            if self.time_percentage in range(91, 101):
                time_for_each_question = test_time[0] / no_of_questions - 5
            else:
                time_for_each_question = test_time[0] / no_of_questions
            self.choose_options(no_of_questions, time_for_each_question, answers, correct_answers)
        else:
            time_for_each_question = test_time[0] / no_of_questions - 15 #should change the -15 if type code is given
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
            answer = answers[str(question)].lower()        
                
            xpaths = [
                '//*[@id="drawer-container"]/div/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[3]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p'
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
                    pass
                
            
            sleep(time_for_each_question)            

            try:
                next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                next_button.click()
            except:
                warning_ok_button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button')
                warning_ok_button.click()
                sleep(.5)

                next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
                next_button.click()

            sleep(2)

    def type_codes(self, no_of_questions, time_for_each_question):
        
        for question in range(1, no_of_questions + 1):
            #typing_field_xpath = '//*[@id="editor"]/textarea'
            #typing_field = self.browser.find_element(By.XPATH, typing_field_xpath)
            #typing_field.click()
            #typing_field.send_keys('#include<stdio.h>')
            sleep(time_for_each_question)
            

            next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')

            next_button.click()
            sleep(7)


        
    def end_test(self, test, test_time, answered):
        #sleep(test_time)
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
            self.logger.log_end_test(len(self.get_json('TestStatus')['COMPLETED']))
            self.update_test_status(test, True)
        else:
            self.logger.log_no_answers()


    def end_test2(self,test):
        
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

        with open('TestStatus.json', 'w') as json_file:
            json.dump(test_status, json_file)
            
    print('\nDEVELOPED BY The DG')
    print("READ THE '_README.txt' file before using this application for ease of access" )
    option = input("\n1. Start / Resume test\n2. Reset test progress\n3. Change user (test progress will be reset)\n4. Set Correct answer percentage\n5. Set Completion time percentage\n6. Choose to attend c programming test (without answers)\n\nYOUR OPTION : ")
    
    if option == '1':
        with open('Student.json', 'r') as file:
            student = json.load(file)
        if student['email'] == '':
            for i in range(3):
                email = input('Email : ')
                if email[-15:] != '@kcgcollege.com':
                    print('\nEnter a valid email')
                    continue
                else:
                    student['email'] = email
                    break
            else:
                return
            pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
            if pwd == '':
                pwd = 'vidhai'

            student['password'] = pwd

            with open('Student.json', 'w') as json_file:
                json.dump(student, json_file)

            

        t = Talentely(student['email'], student['password'], student['answer-percentage'], student['time-percentage'], student['attend-c-test'])       
        try:
            t.login()
        except Exception as exception:
            print('\nSome Error Occured at login')

        print('\nAutomation Started\n')
        t.perform_tests()
    
    elif option == '2':

        reset_status()

        print('\nTEST PROGRESS HAS BEEN RESET\n')
        
    elif  option == '3':
        student = {} 

        for i in range(3):
            email = input('Email : ')
            if email[-15:] != '@kcgcollege.com':
                print('\nEnter a valid email')
                continue
            else:
                student['email'] = email
                break
        else:
            return
        pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
        if pwd == '':
            pwd = 'vidhai'
        student['password'] = pwd
        with open('Student.json', 'w') as json_file:
            json.dump(student, json_file)
        
        reset_status()
        print('STUDENT DETAILS HAS BEEN UPDATED and progress has been reset')
    
    elif option == '4':

        with open('Student.json', 'r') as file:
            student = json.load(file)

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

        student['answer-percentage'] = percentage

        with open('Student.json', 'w') as json_file:
            json.dump(student, json_file)
    
    elif option == '5':
        with open('Student.json', 'r') as file:
            student = json.load(file)

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

        student['time-percentage'] = percentage

        with open('Student.json', 'w') as json_file:
            json.dump(student, json_file)

    elif option == '6':
        with open('Student.json', 'r') as file:
            student = json.load(file)
        
        student['attend-c-test'] = True

        with open('Student.json', 'w') as json_file:
            json.dump(student, json_file)

    
    else:
        print('ENTER VALID OPTION')

if __name__ == '__main__':
    main()
    