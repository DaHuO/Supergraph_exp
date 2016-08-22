import atexit

in_file = None  # type: file
out_file = None  # type: file

case_no = 1


def file_input():
    """
    Replacement for the default input() and raw_input() functions to read from input.txt instead
    """

    global in_file

    if in_file is None:
        in_file = open('input.txt')

    return in_file.readline()


def file_output(obj):
    """
    Output obj to output.txt
    """

    global out_file, case_no

    if out_file is None:
        out_file = open('output.txt', 'w')

    out_file.write('Case #{0}: {1}'.format(case_no, str(obj)) + '\n')
    case_no += 1


def exit_handler():
    """
    Closes all files and resets all variables before exiting so that they are flushed and closed properly
    """

    global in_file, out_file, case_no

    if in_file is not None:
        in_file.close()
        in_file = None

    if out_file is not None:
        out_file.close()
        out_file = None

    case_no = 1


def get_delimited_int_list(delimiter=' '):
    return [int(x) for x in raw_input().split(delimiter)]


atexit.register(exit_handler)

input = raw_input = file_input

print_file = file_output
