#
# problemB.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

# Parser
def parser(fin):
    S = fin.readWord()
    return S

# Solver
# def flip(S,i):
    # print 'flip',S,i
    # N = len(S)-1
    # while S[N] == '+':
        # N -= 1

    # if i == len(S)-1 and i > 0:
        # i -= 1
        # if N == len(S)-1:
            # N -= 1

    # print i,N
    # print S[:i+1][::-1],S[N+1:],'=>',map(lambda s: {'+':'-','-':'+'}[s], S[:i+1][::-1]) + S[N+1:]

    # return map(lambda s: {'+':'-','-':'+'}[s], S[:i+1][::-1]) + S[N+1   :]
    # return S[:i] + map(lambda s: {'+':'-','-':'+'}[s], S[i:][::-1])

def flip(S, count=0):

    # print 'flip:',S,count

    # No pancakes need to be flipped
    if not '-' in S:
        return count

    # All pancakes need to be flipped
    if not '+' in S:
        return count + 1

    # Pancake at bottom is correct, i.e. wil never need to be flipped
    if S[-1] == '+':
        return flip(S[:-1],count)

    # Pancake at bottom is incorret, we should flip all pancakes
    # but if the pancake at the top is already correct it and all
    # pancakes directly after it that is also correct need to be
    # flipped first

    # First panckae (which will be at the bottom will be correct
    # after the flip
    if S[0] == '-':
        S = S[::-1]
        S = map(lambda s: {'+':'-','-':'+'}[s], S)
        return flip(S,count+1)

    # First pancake is already correct and will be incorrect when flipped
    i = 0
    while S[i] == '+':
        S[i] = '-'
        i += 1
    return flip(S,count+1)

def solver(data):
    S = list(data)
    count = flip(S)
    # print 'count:', count
    return count


# Main
if __name__ == '__main__':
    with Timer('Problem B'):
        Problem(parser, solver).run()
