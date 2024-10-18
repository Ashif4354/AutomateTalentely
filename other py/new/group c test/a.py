from json import dump, load


with open('Alltests.json', 'r') as file:
    tests = load(file)['TESTS']

grouped_tests = {}
count = 1
for test in tests:
    print(count)
    if test[2] not in grouped_tests:
        grouped_tests[test[2]] = [test]

    else:
        grouped_tests[test[2]].append(test)
    
    count += 1


# print(grouped_tests)

sorted_test_names = sorted(grouped_tests.keys())
sorted_grouped_tests = {}

for test_name in sorted_test_names:
    sorted_grouped_tests[test_name] = grouped_tests[test_name]


with open('CTests.json', 'w') as file:
    dump(sorted_grouped_tests, file, indent=4)