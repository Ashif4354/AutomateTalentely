from pymongo import MongoClient
from json import dump
from os import system, getenv
from sys import exit
from datetime import datetime
from requests import post

class MongoDbConfig:
    def __init__(self):
        self.mongodburl = 'mongodb+srv://ats:atspassword@atlascluster.ahffbt1.mongodb.net/'

    def connect(self):
        self.client = MongoClient(self.mongodburl)
        self.db = self.client['ATS']
    
    def disconnect(self):
        self.client.close()

def send_update_complete_embed(version):
    url = ''
    
    username = getenv('USERNAME')
    time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        'embeds' : [
            {
                'title' : 'ATS Update Completed',
                'description' : f'At: {time}\nUsername: {username}\nNew Version: {version}',
                'color' : 0xffffff
            }
        ]
    }

    try:
        post(url, headers = headers, json = data)
    except Exception:
        return
        
def update_files():
    mongodb = MongoDbConfig()
    mongodb.connect()
    db = mongodb.db['Latest Version']

    files = db.find_one({'_id': 'ats_files'})

    # del files['_id']
    # del files['version']

    ats_part1 = db.find_one({'_id': 'ats_part_1'})['data']
    ats_part2 = db.find_one({'_id': 'ats_part_2'})['data']

    with open('Automate_Talentely.exe', 'wb') as file:
        file.write(ats_part1 + ats_part2)
    
    for file in files['files_and_types']:

        with open(file + '.' + files['files_and_types'][file], 'w') as f:
            dump(files[file], f, indent=4)

    mongodb.disconnect()
    return files['version']

if __name__ == '__main__':
    print('\nUpdating files...')
    print('Please wait. Do not close this window. This wont take long...')
    
    version = update_files()
    send_update_complete_embed(version)

    system('start Automate_Talentely')
    exit()