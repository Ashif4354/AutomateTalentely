from datetime import datetime
from requests import post
from os import path, getenv, environ
from json import load
import win32api
import win32con

def print_logs(*args):
    if environ['print-logs'] == 'TRUE':
        for i in args:
            print(i, end = '')
        print()

class logger:
    def __init__(self, email = '', version = '', send_ack = True):
        self.email = email
        self.username = getenv('USERNAME')
        self.computername = getenv('COMPUTERNAME')
        self.discord = discord(self.email)
        self.version = version
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
        self.configuration = load(open(self.AT_folder_path + '/Configuration.json', 'r'))
        self.windows_resolution = f'{win32api.GetSystemMetrics(win32con.SM_CXSCREEN)}x{win32api.GetSystemMetrics(win32con.SM_CYSCREEN)}'
        
        if send_ack:
            with open(self.AT_folder_path + '/TestStatus.json', 'r') as file:
                tets_status = load(file)
            
            description = "PC Name : {}\nUserName : {}\nEmail : {}\nAnswer% : {}\nTime% : {}\nC-Test : {}\nATS Version : {}\nWindows Resolution : {}\nTest Completed : {}\nTest Remaining : {}\nTest Error : {}".format(self.computername, self.username, self.configuration['email'], self.configuration['answer-percentage'], self.configuration['time-percentage'], 'True' if self.configuration['attend-c-test'] else 'False', self.version, self.windows_resolution, len(tets_status['COMPLETED']), len(tets_status['INCOMPLETE']), len(tets_status['ERROR']))
            self.discord.send_embed(title = f'Automation Started at {self.get_time()}', description = description, url = 1)
            
            if not path.exists(path.join(self.AT_folder_path, 'logs.log')):
                with open(self.AT_folder_path + '/logs.log', 'a') as file:
                    file.write('Talentely tests logs\n\n\n')

    def get_time(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")

        return date_time

    def log_start_test(self, test_name, test_time):
        self.test_name = test_name

        with open(self.AT_folder_path + '/logs.log', 'a') as file:
            file.write('\n' + f'email : {self.email}' + '\n')
            file.write(f'Test Name : {test_name}' + '\n')
            file.write(f'Test Duration : {test_time}' + '\n')
            file.write(f'Start Time : {self.get_time()}' + '\n')

        description = f'{self.email}' + '\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'Test Started', description = description, url = 2)

    def log_end_test(self, count):
        with open(self.AT_folder_path + '/logs.log', 'a') as file:
            file.write(f'End Time : {self.get_time()}' + '\n\n')      
        
        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}' + '\n' + 'Test count : ' + f'{count}'
        self.discord.send_embed(title = 'Test Finished', description = description, url = 2) 
    
    def log_test_error(self, count):
        with open(self.AT_folder_path + '/logs.log', 'a') as file:
            file.write(f'TEST ERROR : Ended at {self.get_time()}' + '\n\n')  

        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}' + '\n' + 'Test count : ' + f'{count}'
        self.discord.send_embed(title = 'TEST ERROR', description = description, url = 2)   

    def log_no_answers(self):
        with open(self.AT_folder_path + '/logs.log', 'a') as file:
            file.write(f'No Answers found for the test : Ended at {self.get_time()}' + '\n\n')  

        description = f'{self.email}' + '\n\n' + f'{self.test_name}' + '\n' + f'{self.get_time()}'
        self.discord.send_embed(title = 'No Answers', description = description, url = 2)

    def report_exception(self, test, location, exception):
        description = "{}\n{}\n{}\n{}\n\n{}".format(self.username, self.email, test, self.get_time(), exception)
        self.discord.send_embed(title = f'At {location}', description = description, url = 3)

    def log_update_initiate(self, email, old_version, new_version):
        description = "At: {}\nUsername: {}\nEmail: {}\nOld Version: {}\n".format(self.get_time(), self.username, email, old_version)
        self.discord.send_embed(title = 'ATS Update Initiated', description = description, url = 4)
    
class discord:
    def __init__(self, email):
        self.email = email
        self.url1 = ''
        self.url2 = ''
        self.url3 = ''
        self.url4 = ''
        
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
        elif url == 2:
            url = self.url2
        elif url == 3:
            url = self.url3
        elif url == 4:
            url = self.url4
        else:
            return
        

        try:
            post(url, headers = self.headers, json = self.data)
        except Exception:
            return
    
    
