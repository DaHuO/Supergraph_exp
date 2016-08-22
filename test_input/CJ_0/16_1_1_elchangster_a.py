
def run_case(given_string):
    # Get first letter.
    new_string = given_string[0]
    given_string = given_string[1:]

    while (len(given_string) > 0):
        letter = given_string[0]
        given_string = given_string[1:]
        if (letter >= new_string[0]):
            new_string = letter + new_string
        else:
            new_string = new_string + letter
    return new_string


def run(file_name):
    f = open(file_name + ".in", "r")
    g = open(file_name + ".out", "w")
    
    num_test_cases = int(f.readline())
    for case_no in range(1, num_test_cases + 1):
        line = f.readline().rstrip()
        message = "Case #" + str(case_no) + ": " + run_case(line)
        print message
        g.write(message + "\n")

run("A-large")
