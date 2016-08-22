
from itertools import permutations

def permutations(string, step = 0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print "".join(string)

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]
        print string_copy
        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print string_copy
        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)


def before(ch,i):
    return (ch + list[list.index(i)])
def after(ch,i):
    return (list[list.index(i)] + ch)

num_cases = int(raw_input())  # read a line with a single integer
for i in xrange(1, num_cases + 1):
    letters = str(raw_input())
    list = [letters[0]]
    tmp_list = []
    #print list

    for ch in letters[1:]:
        tmp_list = []
        for word in list:
            tmp_list.append(before(ch,word))
            tmp_list.append(after(ch,word))
        list = tmp_list

    list = sorted(list)
    win = list[len(list)-1]



    print "Case #{}:    {}".format(i, win)
