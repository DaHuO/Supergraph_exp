import itertools

handle = open("input.pancakes.txt", "r")

for i in range(int(handle.readline())):
    pancakes = handle.readline().rstrip()
    num_flips = len(tuple(itertools.groupby(pancakes)))
    if pancakes[-1] == "+":
        num_flips -= 1
    print "CASE #{0}: {1}".format(i + 1, num_flips)