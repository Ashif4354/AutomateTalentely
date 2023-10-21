from pymongo import MongoClient
from json import dump
from os import system
from sys import exit

class MongoDbConfig:
    def __init__(self):
        self.mongodburl = 'mongodb+srv://ats:atspassword@atlascluster.ahffbt1.mongodb.net/'

    def connect(self):
        self.client = MongoClient(self.mongodburl)
        self.db = self.client['ATS']
    
    def disconnect(self):
        self.client.close()

def update_files():
    mongodb = MongoDbConfig()
    mongodb.connect()
    db = mongodb.db['Latest Version']

    files = db.find_one({'_id': 'ats_files'})

    # del files['_id']
    # del files['version']

    ats_part1 = db.find_one({'_id': 'ats_part_1'})['data']
    ats_part2 = db.find_one({'_id': 'ats_part_2'})['data']

    with open('ATS.exe', 'wb') as file:
        file.write(ats_part1 + ats_part2)
    
    for file in files['files_and_types']:

        with open(file + '.' + files['files_and_types'][file], 'w') as f:
            dump(files[file], f, indent=4)

    mongodb.disconnect()

if __name__ == '__main__':
    print('\nUpdating files...')
    print('Please wait. Do not close this window. This wont take long...')
    update_files()
    system('start Automate_Talentely')
    exit()