""" imports """
#pylint: disable=W0622
#pylint: disable=E0102
import glob, pickle, os, time, sys, argparse
from copy import copy
import math

""" global variables """

""" classes """
class Bools(object):
    bools = None
    counter = 0

    def __init__(self, bools):
        self.bools = bools

    def __getitem__(self, i):
        return self.bools[i]

    def size(self):
        return len(self.bools)

    def is_empty(self):
        return not self.bools

    def trim_bottom(self):
        num_bools_at_end = self.count_at_end(True)
        if num_bools_at_end:
            self.bools = self.bools[:-num_bools_at_end]

    def count_at_front(self, value):
        counter = 0
        for elem in self.bools:
            if elem == value:
                counter += 1
            else:
                break
        return counter

    def count_at_end(self, value):
        counter = 0
        for elem in reversed(self.bools):
            if elem == value:
                counter += 1
            else:
                break
        return counter

    def apply_swap(self, num_to_swap):
        assert 0 < num_to_swap <= len(self.bools), num_to_swap
        first_part = self.bools[:num_to_swap]
        swapped = [not b for b in reversed(first_part)]
        self.bools = swapped + self.bools[num_to_swap:]
        self.trim_bottom()
        self.counter += 1

    def __str__(self):
        return ''.join('+' if b else '-' for b in self.bools)

    def __repr__(self):
        return self.__str__()
    

""" functions """
def solve(line):
    bools = Bools([c == "+" for c in line.strip()])
    bools.trim_bottom()
    while not bools.is_empty():
        if bools[0] == True:
            bools.apply_swap(bools.count_at_front(True))
        else:
            bools.apply_swap(bools.size())
    return bools.counter


def main():
    ### parse input ###
    ## parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="default.in", nargs='?')
    parser.add_argument("-t", "--test", action="store_true")
    parser.add_argument("-l", "--lazytest", action="store_true")
    args = parser.parse_args()
    output = ""
    TIC = time.time()

    ## read input lines
    input_lines = open(args.filename).readlines()
    def read_line():
        return input_lines.pop(0).strip()
    def read_ints():
        return [int(x) for x in read_line().split(' ')]
    def read_floats():
        return [float(x) for x in read_line().split(' ')]
    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):
        ### parse input ###
        line = read_line()

        ### calculate answer ###
        answer = solve(line)
        assert answer != None

        ### output ###
        #print "Calculating case #{}...".format(questionindex+1)
        answer_str = "Case #{}: {}".format(questionindex+1, answer)
        output += answer_str + '\n'
        print answer_str

    ## write output
    ofile = open('output', 'w').write(output)
    TOC = time.time()
    #print "done in {} s".format(TOC-TIC)


    ### test ###
    if args.test:
        def filter_extension(filename):
            filename_parts = filename.split('.')
            if len(filename_parts) > 1:
                filename_parts = filename_parts[:-1]
            return '.'.join(filename_parts)

        print
        print "== TESTING VALIDITY =="

        try:
            # check if all input was used
            assert not len([l for l in input_lines if l.strip()]), "Not all input was used"

            # filter extension of filename
            filename_without_extension = filter_extension(args.filename)

            # get calculated and correct lines
            calculated_lines = [l.strip() for l in output.split('\n') if l.strip()]
            correct_lines = [l.strip() for l in open("{}.out".format(filename_without_extension)).readlines() if l.strip()]

            # check if number of lines match
            assert len(correct_lines) == len(calculated_lines), "calculated {} lines but expected {}".format(len(calculated_lines), \
                                                                len(correct_lines))

            # apply lazytest: filter away test numer
            unfiltered_calculated_lines = calculated_lines
            unfiltered_correct_lines = correct_lines
            if args.lazytest:
                def filter_test_number(line):
                    if line.startswith("Case #"):
                        parts = line.split('#')
                        parts[1] = parts[1][parts[1].index(':'):]
                        return '#'.join(parts)
                    else:
                        return line
                calculated_lines = [filter_test_number(l) for l in calculated_lines]
                correct_lines = [filter_test_number(l) for l in correct_lines]

            # get lines that don't match
            incorrect_line_numbers = []
            for line_number, (correct_line, calculated_line) in enumerate(zip(correct_lines, calculated_lines)):
                if correct_line != calculated_line:
                    incorrect_line_numbers.append(line_number)
            if len(incorrect_line_numbers):
                error_msg = "\n"
                for line_number in incorrect_line_numbers:
                    error_msg += '    "{}"  should be  "{}"\n'.format(unfiltered_calculated_lines[line_number],
                                                                      unfiltered_correct_lines[line_number])
                raise AssertionError(error_msg)

            print "SUCCESS"

        except AssertionError as ex:
            print "\nFAILED:"
            print str(ex)
        print


if __name__ == '__main__':
    main()
