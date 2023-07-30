from datetime import datetime
from requests import post
from os import path, getenv
from json import load

class logger:
    def __init__(self, email, version):
        self.email = email
        self.username = getenv('USERNAME')
        self.discord = discord(self.email)
        self.version = version
        self.AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
        self.configuration = load(open(self.AT_folder_path + '/Configuration.json', 'r'))
        
        description = "UserName : {}\nEmail : {}\nAnswer% : {}\nTime% : {}\nC-Test : {}\nVersion : {}".format(self.username, self.configuration['email'], self.configuration['answer-percentage'], self.configuration['time-percentage'], 'True' if self.configuration['attend-c-test'] else 'False', self.version)
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

    def report_exception(self, test, location, exception):
        description = "{}\n{}\n{}\n{}\n\n{}".format(self.username, self.email, test, self.get_time(), exception)
        self.discord.send_embed(title = f'At {location}', description = description, url = 3)


class discord:
    def __init__(self, email):
        self.email = email
        self.url1 = 'https://discord.com/api/webhooks/1132211379923853322/IbcrftADhJrMmJL-Y_lha1FXc0edPd-HpxXPjBOVwJ4iDWj4joz0dh-b6cc_J-yNzMYg'
        self.url2 = 'https://discord.com/api/webhooks/1132233451567857694/LGnPeaWId7Xa-1NxL70bCDzB-wW6FbDvw7LCTI76m5nMvBUXLUhYBBy7SdLg9Q8kAJGO'
        self.url3 = 'https://discord.com/api/webhooks/1134892597668753448/RaoYzDR_O6P07whGZ_GiSJnT2j4p3HRgHisSaJ31TeAo5VHCstYOTBFymq6Nher1jlUI'
        
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
        else:
            return

        try:
            post(url, headers = self.headers, json = self.data)
        except Exception:
            return
    
    
