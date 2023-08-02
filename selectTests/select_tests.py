from flask import Flask, request
from json import loads, dump
from threading import Thread
from logging import getLogger,CRITICAL
from os import getcwd, getenv

from flask_cors import CORS

select_tests_app = Flask(__name__)
CORS(select_tests_app)

log = getLogger('werkzeug')
log.setLevel(CRITICAL)
select_tests_app.logger.disabled = True

@select_tests_app.route("/", methods=['POST'])
def select_tests_():
    tests = loads(request.data.decode('utf-8'))
    with open(getcwd().rstrip('selectTests') + '/jsonFiles/tests.json', 'w') as json_file:
        dump(tests, json_file)

    test_status = {
        'COMPLETED' : [],
        'INCOMPLETE' : [],
        'ERROR' : []
    }

    with open(f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely", 'w') as file:
        dump(test_status, file)


    return 'Tests Updated'
    
    
class a(Thread):
    def run(self):
        select_tests_app.run()
    
if __name__ == "__main__":
    thr = a()
    thr.start()