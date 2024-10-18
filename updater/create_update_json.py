from json import load
from pymongo import MongoClient
from os import getcwd
from sys import path

path.append(getcwd().rstrip('updater'))
from Talentely import AT

class MongoDbConfig:
    def __init__(self):
        self.mongodburl = ''

    def connect(self):
        self.client = MongoClient(self.mongodburl)
        self.db = self.client['ATS']
    
    def disconnect(self):
        self.client.close()


with open('../jsonFiles/tests.json', 'r') as file:
    tests = load(file)

with open('../jsonFiles/Answers.json', 'r') as file:
    answers = load(file)

with open('../jsonFiles/Ctests.json', 'r') as file:
    ctests = load(file)

with open('../jsonFiles/Qtests.json', 'r') as file:
    qtests = load(file)

with open('../jsonFiles/Rtests.json', 'r') as file:
    rtests = load(file)

with open('../jsonFiles/Vtests.json', 'r') as file:
    vtests = load(file)

with open('../text files/_README.txt', 'r') as file:
    readme = file.read()

with open('../output/Automate_Talentely.exe', 'rb') as file:
    ats = file.read()

updates_for = []

mongodb = MongoDbConfig()
mongodb.connect()
collection = mongodb.db['Latest Version']


current_verion_in_development = {
    '_id': 'ats_files',
    'version': AT().version,
    'files_and_types': {
        'tests': 'json', 
        'Answers': 'json', 
        'Ctests': 'json', 
        'Qtests': 'json', 
        'Rtests': 'json', 
        'Vtests': 'json', 
        '_README': 'txt'
        },
    'tests': tests,
    'Answers': answers,
    'Ctests': ctests,
    'Qtests': qtests,
    'Rtests': rtests,
    'Vtests': vtests,
    '_README': readme,
}
def create_document():
    collection.insert_one(current_verion_in_development)
    collection.insert_one({'_id': 'ats_part_1', 'version': AT().version, 'data': ats[:len(ats) // 2]})
    collection.insert_one({'_id': 'ats_part_2', 'version': AT().version, 'data': ats[len(ats) // 2:]})

    mongodb.disconnect()

def update_document():
    query1 = {'_id': 'ats_files'}
    update1 = {'$set': current_verion_in_development}

    query2 = {'_id': 'ats_part_1'}
    update2 = {'$set': {'version': AT().version, 'data': ats[:len(ats) // 2]}}

    query3 = {'_id': 'ats_part_2'}
    update3 = {'$set': {'version': AT().version, 'data': ats[len(ats) // 2:]}}

    collection.update_one(query1, update1, upsert=True)
    collection.update_one(query2, update2, upsert=True)
    collection.update_one(query3, update3, upsert=True)

    mongodb.disconnect()


if __name__ == '__main__':
    # create_document()
    update_document()
    