from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import json

from logger import logger

class Talentely:
    def __init__(self, email, password = 'vidhai'):
        self.url = 'https://system.talentely.com/login'
        self.browser  = None
        self.email = email
        self.password = password
        self.tests = None
        self.incomplete_tests = None
        self.logger = logger(self.email)
        
    def open_browser(self):
        self.browser = webdriver.Edge()
        self.browser.maximize_window()    

    def login(self):
        self.open_browser()
        self.browser.get(self.url)
        sleep(1)

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
            if not test in test_status['COMPLETED'] and test not in test_status['INCOMPLETE']:
                test_status['INCOMPLETE'].append(test)

        self.incomplete_tests = test_status['INCOMPLETE']

        with open('TestStatus.json', 'w') as json_file:
            json.dump(test_status, json_file)

    def update_test_status(self, test):
        test_status = self.get_json('TestStatus')

        test_status['COMPLETED'].append(test)
        test_status['INCOMPLETE'].remove(test)

        with open('TestStatus.json', 'w') as json_file:
            json.dump(test_status, json_file)

    def perform_tests(self):
        self.generate_test_status()        

        for test in self.incomplete_tests:
            self.navigate_home_page(test)

    def navigate_home_page(self, test):
        
        if test[0] == 'a':
            aptitude_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button')
            aptitude_button.click()
            sleep(2)
            self.navigate_aptitude(test)

        elif test[0] == 'c':
            c_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/button')
            c_button.click()
            sleep(2)
            self.navigate_c(test)
            
        else:
            pass
    
    def navigate_aptitude(self, test):
        if test[1] == 'q':
            quantitative_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
            quantitative_button.click()
            sleep(2)

        elif test[1] == 'r':
            reasoning_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a')
            reasoning_button.click()
            sleep(2)

        elif test[1] == 'v':
            verbal_button = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a')
            verbal_button.click()
            sleep(2)

        else:
            pass
        
        self.find_and_do_test(test)

    def navigate_c(self, test):
        basic_c = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
        basic_c.click()
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
        
        total_time -= 30
        return (total_time, test_time)

    def find_and_do_test(self, test):

        test_xpath = self.get_test_xpath(test)
        
        test_button = self.browser.find_element(By.XPATH, test_xpath)
        self.browser.execute_script('arguments[0].scrollIntoView(true);', test_button)       
        test_button.click()
        sleep(2)

        test_button_2 = self.browser.find_element(By.ID, f'stepper{test[3]}')
        test_button_2.click()
        sleep(2)

        test_name = self.browser.find_element(By.XPATH, f'//*[@id="stepper{test[3]}"]/span/span[2]/span').text

        body = self.browser.find_element(By.XPATH, '/html/body')
        body.click()
        sleep(3)

        test_time = self.get_test_time(test)

        start_test_button = self.browser.find_element(By.XPATH, f'//*[@id="height{test[3] - 1}"]/div/div/div/button/span[1]')
        
        self.start_test(start_test_button, test_name, test_time[1])        

        end_test_button = self.browser.find_element(By.XPATH, '//*[@id="FullScreen"]/div[2]/div/div[3]/button[6]')
        
        self.end_test(test, end_test_button, test_time[0])
    
    def start_test(self, start_button, test_name, test_time):
        start_button.click()
        self.logger.log_start_test(test_name, test_time)

        sleep(5)
    
    def end_test(self, test, end_button, test_time):
        sleep(5)

        end_button.click()
        sleep(1)        

        submit_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        submit_button.click()
        sleep(2)

        cancel_button = self.browser.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')
        cancel_button.click()
        sleep(1)

        self.logger.log_end_test()
        self.update_test_status(test)

def main():
    email = input('Email : ')

    if email[-15:] != '@kcgcollege.com':
        print('\nEnter a valid email')
        return

    t = Talentely(email) 
    try:
        t.login()
    except Exception as exception:
        print('\nSome Error Occured')

    print('\nAutomation Started')
    t.perform_tests()


if __name__ == '__main__':
    main()
    