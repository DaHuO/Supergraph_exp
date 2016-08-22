import numpy as np

def flip(c, n):
    """c must be np.array"""
    c[:n] = (~c[:n])[::-1]
    return c

def make_it_happy(pans):
    count = 0
    while not pans.all():
        x = np.logical_xor(pans, np.roll(pans, -1))
        ind = np.where(x)
        try:
            ind = ind[0][0] + 1
        except IndexError:
            ind = len(pans)
        pans = flip(pans.copy(), ind)
        count += 1
    return count

with open("B-large.in") as infile:
    with open("pans-large.out", "w+") as outfile:
        num_cases = int(infile.readline())

        for row in range(1, num_cases + 1):
            cakes = np.array([True if item == "+" else False for item in list(infile.readline().strip())])
            res = make_it_happy(cakes)
            outfile.write("Case #{0}: {1}\n".format(row, res))
