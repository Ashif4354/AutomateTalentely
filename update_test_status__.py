import json

with open('TestStatus.json', 'r') as json_file:
    testsstatus = json.load(json_file)


new_tests = {'COMPLETED' : [], 'INCOMPLETE' : [], 'ERROR' : []}

with open('tests.json', 'r') as json_file:
    test_with_names = json.load(json_file)

for i in testsstatus.keys():
    for j in testsstatus[i]:
        #print(j)
        test = j

        for k in test_with_names['TESTS']:
            print(k[:4])
            if test == k[:4]:
                print('HELLLLLLLLLLLLLLLLo')
                
                new_tests[i].append(k)
        #input("WAAIT")


with open('TestStatus.json', 'w') as file:
    json.dump(new_tests, file)
        

