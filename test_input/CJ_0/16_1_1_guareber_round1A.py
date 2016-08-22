import sys


def load_testcase(filename):

    with open(filename, 'r') as f:
        num_cases = int(f.readline().rstrip('\n'))
        cases = []
        for i in range(num_cases):
            line = f.readline().rstrip('\n')
            cases.append(line)
        return cases


def place_character(string, character):
    if (character >= string[0]):
        return character + string
    else :
        return string + character


if __name__ == "__main__":
    print(sys.argv[1])

    test_cases = load_testcase(sys.argv[1])
    counter = 1
    for test in test_cases:
        string = ''
        for character in test:
            if string == '':
                string = character
            else :
                string = place_character(string, character)

        print('Case #' + str(counter) + ': ' + string)
        counter += 1

