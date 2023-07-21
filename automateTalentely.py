from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class Talentely:
    def __init__(self, email, password = 'vidhai'):
        self.url = 'https://system.talentely.com/login'
        self.browser  = None
        self.email = email
        self.password = password
        

    '''
    class Student:
        def __init__(self, email):
            self.email = ''
            self.password = 'vidhai'
    '''
    def open_browser(self):
        self.browser = webdriver.Edge()

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
        #A Q jss2329 (2, 3, 4)
        a = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/button')
        a.click()

        sleep(3)
 
        a = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
        a.click()

        sleep(3)
 
        a = self.browser.find_element(By.XPATH, '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a')
        a.click()
        
        sleep(3)

        a = self.browser.find_element(By.ID, 'stepper1')
        a.click()

        sleep(3)
 
        a = self.browser.find_element(By.XPATH, '/html/body')
        a.click()

        sleep(3)
 
        a = self.browser.find_element(By.XPATH, '//*[@id="height0"]/div/div/div/button/span[1]')
        a.click()

        sleep(50)


        
        

#/html/body
#//*[@id="height0"]/div/div/div/button
#//*[@id="height1"]/div/div/div/button
#//*[@id="height2"]/div/div/div/button



if __name__ == '__main__':
    t = Talentely('20cs008@kcgcollege.com')
    t.login()