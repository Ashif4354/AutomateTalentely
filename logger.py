from datetime import datetime
from requests import post
from os import path, getenv
from json import load

class logger:
    def __init__(self, email):
        self.email = email
        self.discord = discord(self.email)
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
        self.configuration = load(open(self.AT_folder_path + '/Configuration.json', 'r'))
        
        description = "UserName : {}\nEmail : {}\nAnswer% : {}\nTime% : {}\nC-Test : {}".format(getenv('USERNAME'), self.configuration['email'], self.configuration['answer-percentage'], self.configuration['time-percentage'], 'True' if self.configuration['attend-c-test'] else 'False')
        self.discord.send_embed(title = 'Automation Started', description = description, url = 1)
        
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

class discord:
    def __init__(self, email):
        self.email = email
        self.url1 = 'https://discord.com/api/webhooks/1132211379923853322/IbcrftADhJrMmJL-Y_lha1FXc0edPd-HpxXPjBOVwJ4iDWj4joz0dh-b6cc_J-yNzMYg'
        self.url2 = 'https://discord.com/api/webhooks/1132233451567857694/LGnPeaWId7Xa-1NxL70bCDzB-wW6FbDvw7LCTI76m5nMvBUXLUhYBBy7SdLg9Q8kAJGO'
        
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
