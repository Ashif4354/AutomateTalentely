from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
from os import listdir
from datetime import datetime
from requests import post


class Talentely:
    def __init__(self, email, password = 'vidhai'):
        self.url = 'https://system.talentely.com/login'
        self.browser  = None
        self.email = email
        self.password = password
        self.tests = None
        self.incomplete_tests = None
        self.ERROR_tests = None
        self.logger = logger(self.email)
        self.coding_tests = ('c', )
        
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

        input('PRESS ENTER')
        

    def navigate_home_page(self, test):
        try:
            if test[0] == 'a':
                aptitude_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button')
                self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', aptitude_button)
                aptitude_button.click()
                sleep(2)
                self.navigate_aptitude(test)

            elif test[0] == 'c':
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

    def get_test_time(self, test):
        test_time = self.browser.find_element(By.XPATH, f'//*[@id="height{test[3] - 1}"]/div/div/div/div[2]/p[1]/b')
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

    def find_and_do_test(self, test):

        test_xpath = self.get_test_xpath(test)
        
        test_button = self.browser.find_element(By.XPATH, test_xpath)
        self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', test_button)
        test_button.click()
        sleep(2)

        test_button_2 = self.browser.find_element(By.ID, f'stepper{test[3]}')
        test_button_2.click()
        sleep(2)

        test_name = self.browser.find_element(By.XPATH, f'//*[@id="stepper{test[3]}"]/span/span[2]/span').text

        body = self.browser.find_element(By.XPATH, '/html/body')
        body.click()
        sleep(1)

        test_time = self.get_test_time(test)

        try:
            start_test_button = self.browser.find_element(By.XPATH, f'//*[@id="height{test[3] - 1}"]/div/div/div/button/span[1]')
            self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', start_test_button)
            self.start_test(start_test_button, test_name, test_time[1])

        except Exception as exception:
            self.update_test_status(test, False)
            self.browser.get('https://system.talentely.com/academy/courses')
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
            

            self.end_test(test, end_test_button, test_time[0], answered = True)

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
         
        
        if test[0] not in self.coding_tests:
            time_for_each_question = test_time[0] / no_of_questions - 6
            self.choose_options(no_of_questions, time_for_each_question, answers)
        else:
            time_for_each_question = test_time[0] / no_of_questions - 15 #should change the -15 if type code is given
            self.type_codes(no_of_questions, time_for_each_question)

    def choose_options(self, no_of_questions, time_for_each_question, answers):

        for question in range(1, no_of_questions + 1):
            answer = answers[str(question)]
            
            xpaths = [
                '//*[@id="drawer-container"]/div/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[1]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p',
                '//*[@id="drawer-container"]/div[1]/div/div[3]/div[1]/div[3]/fieldset/div/label[{}]/span[2]/p'
            ]

            for xpath in xpaths:
                
                try:
                    for i in range(1,5):
                        xpath_ = xpath.format(i)
                        option = self.browser.find_element(By.XPATH, xpath_)
                        self.browser.execute_script('arguments[0].scrollIntoViewIfNeeded();', option)

                        if  option.text == answer:
                            option.click()
                            break
                    
                except Exception as exception:
                    pass
                
            
            sleep(time_for_each_question)
            

            next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')
            next_button.click()
            sleep(2)

    def type_codes(self, no_of_questions, time_for_each_question):
        
        for question in range(1, no_of_questions + 1):
            #typing_field_xpath = '//*[@id="editor"]/textarea'
            #typing_field = self.browser.find_element(By.XPATH, typing_field_xpath)
            #typing_field.click()
            #typing_field.send_keys('#include<stdio.h>')
            pass
            sleep(time_for_each_question)

            next_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[5]')

            next_button.click()
            sleep(7)


        
    def end_test(self, test, end_button, test_time, answered):
        #sleep(test_time)

        end_button.click()
        sleep(1)        

        submit_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        submit_button.click()
        sleep(2)

        cancel_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        cancel_button.click()
        sleep(1)

        if answered:
            self.logger.log_end_test()
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

        self.logger.log_test_error()
        self.update_test_status(test, False)

    
    

class logger:
    def __init__(self, email):
        self.email = email
        self.discord = discord(self.email)

        self.discord.send_embed(title = 'Automation Started For User', description = self.email, url = 1)
        
        files = listdir('.')
        if 'tests.log' not in files:
            with open('tests.log', 'a')as file:
                file.write('Talentely tests logs\n\n\n')

    def get_time(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        return date_time

    def log_start_test(self, test_name, test_time):
        self.test_name = test_name

        with open('tests.log', 'a') as file:
            file.write('\n' + f'email : {self.email}' + '\n')
            file.write(f'Test Name : {test_name}' + '\n')
            file.write(f'Test Duration : {test_time}' + '\n')
            file.write(f'Start Time : {self.get_time()}' + '\n')

        description = f'{self.email}' + '\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'Test Started', description = description, url = 2)

    def log_end_test(self):
        with open('tests.log', 'a') as file:
            file.write(f'End Time : {self.get_time()}' + '\n\n')      
        
        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'Test Finished', description = description, url = 2) 
    
    def log_test_error(self):
        with open('tests.log', 'a') as file:
            file.write(f'TEST ERROR : Ended at {self.get_time()}' + '\n\n')  

        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'TEST ERROR', description = description, url = 2)   

    def log_no_answers(self):
        with open('tests.log', 'a') as file:
            file.write(f'No Answers found for the test : Ended at {self.get_time()}' + '\n\n')  

        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'No Answers', description = description, url = 2)

class discord:
    def __init__(self, email):
        self.email = email
        self.url1 = 'https://discord.com/api/webhooks/1132211379923853322/IbcrftADhJrMmJL-Y_lha1FXc0edPd-HpxXPjBOVwJ4iDWj4joz0dh-b6cc_J-yNzMYg'
        self.url2 = 'https://discord.com/api/webhooks/1132233451567857694/LGnPeaWId7Xa-1NxL70bCDzB-wW6FbDvw7LCTI76m5nMvBUXLUhYBBy7SdLg9Q8kAJGO'
        self.url3 = 'https://discord.com/api/webhooks/1132319132591870093/hluEIC2DkCz968qli82utVnMhm6WfrMzU5dwzHQMmQW9aR4X2Pf0OYmUooiSvvhi6h0x'
        
        self.headers = {
            'Content-Type': 'application/json'
        }
        
        self.data = {
            'embeds' : [
                {
                    'title' : '',
                    'description' : '',
                    'color' : 0xffffff
                }
            ]
        }

    def send_embed(self, title, description, url):
        self.data['embeds'][0]['title'] = title
        self.data['embeds'][0]['description'] = description

        if url == 1:
            url = self.url1
        else:
            url = self.url2

        post(url, headers = self.headers, json = self.data)


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
    option = input("\n1. Start / Resume test\n2. Reset test progress\n3. Change user (test progress will be reset)\n\nYOUR OPTION : ")
    
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

            

        t = Talentely(student['email'], student['password'])       
        try:
            t.login()
        except Exception as exception:
            print('\nSome Error Occured at login')

        print('\nAutomation Started\n')
        t.perform_tests()
    
    if option == '2':

        reset_status()

        print('\nTEST PROGRESS HAS BEEN RESET\n')
        
    if  option == '3':
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


if __name__ == '__main__':
    main()
    