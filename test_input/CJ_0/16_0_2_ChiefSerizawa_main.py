import sys
import time

f = open(sys.argv[1])
n = int(f.readline())
stacks = f.read().splitlines()

def opti_flip(i, stack):
    while (i >= 0 and stack[i] == '+'):
        i -= 1
    slc = stack[:i+1]

    if len(slc) == 0:
        return i, stack
        
    if slc[0] == '-':
        slc_flipped = ""
        for pck in slc:
            if pck == '+':
                slc_flipped = '-' + slc_flipped
            else:
                slc_flipped = '+' + slc_flipped
        stack = slc_flipped + stack[i+1:]
        return i, stack
    else:
        j = 0
        while slc[j] == '+':
            j += 1
        slc = slc[0:j]
        slc_flipped = ""
        for pck in slc:
            slc_flipped = '-' + slc_flipped
        stack = slc_flipped + stack[j:]
        return i, stack

for idx, stack in enumerate(stacks):
    i = len(stack) - 1
    flips = 0
    while i >= 0:
        i, stack = opti_flip(i, stack)
        flips += 1
    print("Case #%d: %d" % (idx+1, flips-1))
