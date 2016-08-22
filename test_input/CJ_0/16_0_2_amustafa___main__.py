import os, sys, re

def process_input(input_raw):
    num_cases = int(input_raw.pop(0).strip("\n"))
    cases = [i.strip('\n') for i in input_raw]
    return num_cases, cases


def get_output(pancakes_stack):
    #strip all '+' from the bottom of the stack. All problems are equivalent after that point.
    pancakes_stack = pancakes_stack.rstrip('+')
    if len(pancakes_stack) == 0:
        return 0
    else:
        #represents the aggregate transitions that need to occur. and reverses it to make is it in decrease significance.
        transition_command = pancakes_stack.replace("-", "1").replace("+","0")[::-1]
        #get inversions
        inversions = re.split('(0*)', transition_command)
        # if there is a zero at the beginning or the end, there might be an empty space in the array. Removing it.
        if inversions[0] == '':
            inversions.pop(0)
        if inversions[-1] == '':
            inversions.pop(-1)
        return len(inversions)


if __name__ == "__main__":
    VERBOSE = False
    case_file_name = "B-large"
    input_file = os.path.join("input", "{}.in".format(case_file_name))
    with open(input_file, 'r') as f:
        input_data_raw = f.readlines()

    num_cases, cases = process_input(input_data_raw)

    output_array = []
    for case_number in xrange(num_cases):
        if VERBOSE:
            print "Running Problem", case_number
            print "\tInput: ", cases[case_number]
        output_array.append("Case #{}: {}".format(str(case_number+1), str(get_output(cases[case_number]))))
        if VERBOSE:
            print "\tOutput: ", output_array[-1]

    output_txt = "\n".join(output_array)
    output_file = os.path.join("output", "{}.out".format(case_file_name))

    with open(output_file, 'w+') as f:
        f.write(output_txt)

    print "Done"


