from json import dump, load


with open('tests.json', 'r') as json_file:
    tests = load(json_file)


def main():
    new_tests = {}

    for test in tests['TESTS']:
        test[2] = test[2].capitalize()
        if test[2] not in new_tests:
            new_tests[test[2]] = [test]
        else:            
            new_tests[test[2]].append(test)
    
    new_test_keys = new_tests.keys()
    new_tests_keys = sorted(new_test_keys)
    
    new_new_tests = {}
    for test in new_tests_keys:
        new_new_tests[test] = new_tests[test]
        new_new_tests[test].sort()


    

    with open('segregated_tests.json', 'w') as json_file:
        dump(new_new_tests, json_file)

    


if __name__ == '__main__':
    main()