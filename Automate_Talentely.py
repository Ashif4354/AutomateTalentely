from json import dump, load, loads
from os import getcwd, path, system, getenv, makedirs, environ
from requests import get
from selectTests import select_tests
from threading import Thread
from selenium import webdriver
from webbrowser import open_new
from getpass import getpass

from Talentely import Talentely, AT

def main():

    def reset_status():
        test_status = {
            'COMPLETED' : [],
            'INCOMPLETE' : [],
            'ERROR' : []
        }
        with open(AT_folder_path + '/TestStatus.json', 'w') as json_file:
            dump(test_status, json_file)  

    with open(AT_folder_path + '/Configuration.json', 'r') as file:
        configuration = load(file)

    c_test_attend_status = 'ON' if configuration['attend-c-test'] else 'OFF'

    option = input("\n1. Start / Resume test\n2. Reset test progress\n3. Change user (test progress will be reset)\n4. Set Correct answer percentage (Current value : {}%)\n5. Set Completion time percentage (Current value : {}%)\n6. Toggle On/Off to Attend c programming test(without answers)(currently {})\n7. Manually select which tests to attend\n8. Show test status\n\nYOUR OPTION : ".format(configuration['answer-percentage'], configuration['time-percentage'], c_test_attend_status))
    
    if option == '1':
        if configuration['email'] == '':
            for i in range(3):
                email = input('Email : ')
                if email[-15:] != '@kcgcollege.com':
                    print('\nEnter a valid email')
                    continue
                else:
                    configuration['email'] = email
                    break
            else:
                return
            pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
            if pwd == '':
                pwd = 'vidhai'

            configuration['password'] = pwd

            with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
                dump(configuration, json_file)            

        t = Talentely(configuration['email'], configuration['password'], configuration['answer-percentage'], configuration['time-percentage'], configuration['attend-c-test'])       
        try:
            t.login()
        except Exception as exception: #log needed
            print('\nSome Error Occured at login')
            return

        system('cls')
        print('\nAutomation Started\n')
        
        t.perform_tests()
    
    elif option == '2':
        reset_status()
        system('cls')
        print('\n((TEST PROGRESS HAS BEEN RESET))')
        
    elif  option == '3':
        for i in range(3):
            email = input('Email : ')
            if email[-15:] != '@kcgcollege.com':
                print('\nEnter a valid email')
                continue
            else:
                configuration['email'] = email
                break
        else:
            return
        pwd = input("Enter password only if its other than 'vidhai' else press enter : ")
        if pwd == '':
            pwd = 'vidhai'
        configuration['password'] = pwd
        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        reset_status()
        system('cls')
        print('\n((STUDENT DETAILS HAS BEEN UPDATED and progress has been reset))')
    
    elif option == '4':

        try:
            percentage = int(input('Enter approximate percentage of questions you want to be answered correctly for all tests (The default is 100): '))

            if percentage in range(101):
                pass
            else:
                print('Percentage should be from 0 - 100')
                
                return
        except:
            print('Enter valid Percentage')
            return

        configuration['answer-percentage'] = percentage

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        system('cls')
        print('\n((ANSWER PERCENTAGE UPDATED))')
    
    elif option == '5':

        try:
            percentage = int(input('Enter approximate percentage of time you want the application to attend all tests (The default is 100): '))

            if percentage in range(20, 101):
                pass
            else:
                system('cls')
                print('((Percentage should be from 20 - 100))')
                
                return
        except:
            print('Enter valid Percentage')
            return

        configuration['time-percentage'] = percentage

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)

        system('cls')
        print('\n((TIME PERCENTAGE UPDATED))')

    elif option == '6':        
        configuration['attend-c-test'] = True if not configuration['attend-c-test'] else False

        with open(AT_folder_path + '/Configuration.json', 'w') as json_file:
            dump(configuration, json_file)
        
        system('cls')
            
    elif option == '7':
        # browser = webdriver.Edge()
        # browser.get('https://automatetalentely.netlify.app/selecttests')        
        # input()
        system('cls')
        open_new('https://automatetalentely.netlify.app/selecttests')
    
    elif option == '8':
        with open(AT_folder_path + '/TestStatus.json', 'r') as file:
            TestStatus = load(file)

        system('cls')
        print('\nTests Completed : {}\nTests Remaining : {}\nTests Error : {}'.format(len(TestStatus['COMPLETED']), len(TestStatus['INCOMPLETE']), len(TestStatus['ERROR']), ))
    
    elif option == 'admin':
        system('cls')
        password = getpass('Password : ')
        if password != 'fihsa':
            system('cls')
            return
        system('cls')
        option_2 = input('1. Print Logs\n\nYour Option : ')

        if option_2 == '1':
            environ['print-logs'] = 'TRUE'            
        else:
            pass
        system('cls')

    else:
        system('cls')
        print('\nENTER VALID OPTION')

if __name__ == '__main__':
    class flask_server(Thread):
        def run(self):
            select_tests.select_tests_app.run()
    
    flask_server().start()

    environ['print-logs'] = 'FALSE'

    system('cls')


    AT_folder_path = f"C:/Users/{getenv('USERNAME')}/Documents/AutomateTalentely"
    at = AT()
    at.create_configuration_files()
    at.check_update()

    print('\nDEVELOPED BY The DG')
    print("\nCOMPULSORILY READ THE '_README.txt' file present in the installation directory, before using this application for ease of access" )
    print('\nYour PC Display resolution should be 1920 x 1080 and scale should be 100% or else the app may not work as intended')
    print('\nvisit automatetalentely.netlify.app for more..')

    while True:
        main()
        

    