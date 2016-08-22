from bitarray import bitarray
from multiprocessing import Pool

class PC_stack:
    def __init__(self, st_s):
        st = [c_to_int(c) for c in st_s]
        self.st = bitarray(st)

        self.moves = 0

        self.heur_m = -1
    def flip(self, n):
        new_stack = PC_stack('')
        new_stack.moves = self.moves + 1
        new_stack.st = self.st.copy()

        #temp = bitarray([not x for x in reversed(new_stack.st[:n])])
        new_stack.st[:n] = bitarray([not x for x in reversed(new_stack.st[:n])])
        return new_stack

    def flips_mc(self):
        l = range(1, len(self.st) + 1)
        with Pool(4) as p:
            fl = p.map(self.flip, l)
        return fl

    def flips(self):
        fl = []
        for n in range(1, len(self.st) + 1):
            fl.append(self.flip(n))
        return fl

    def is_done(self):
        return sum(self.st) == 0

    def heur(self):
        if self.heur_m != -1:
            return self.heur_m
        h = 0
        c = False
        for b in self.st:
            if c == False and b == True:
                c = True
            if c == True and b == False:
                h += 1
                c = False
        if c == True:
            h += 1

        self.heur_m = self.moves + h
        return self.heur_m

    def __lt__(self, other):
        return self.heur() < other.heur()

def c_to_int(c):
    if c == '+':
        return 0
    elif c == '-':
        return 1
