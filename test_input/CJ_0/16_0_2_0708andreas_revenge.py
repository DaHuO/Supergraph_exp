from sys import *

infile = open("B-large.in", "r")

def flip(l, i):
    """
    Flips the top i elements of the list.
    Returns the flipped list
    """
    to_flip = l[:i]
    rest = l[i:]
    to_flip = [not x for x in to_flip[::-1]]
    return to_flip + rest

#=> flip([False, False, True, False], 2) result [True, True, True, False]

def solve(line):
    cakes = [False if x == "-" else True for x in list(line.strip())]
    flips = 0
    last = cakes[0]
    for x in cakes[1:]:
        if not last == x:
            flips += 1
        last = x
    # while not set(cakes) == set([True]):
    #     i = cakes[::-1].index(False)
    #     cakes = flip(cakes, i + 1)
    #     print(cakes)
    #     flips += 1
    return flips + (1 if list(line.strip())[-1] == "-" else 0)

def main():
    count = int(infile.readline())
    for x in range(count):
        print("Case #" + str(x + 1) + ": " + str(solve(infile.readline())))
        
#=> solve("--+-") result unreachable

#if __name__ == "__main__":
main()