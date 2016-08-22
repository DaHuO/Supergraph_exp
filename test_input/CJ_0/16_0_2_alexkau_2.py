from code_jam import *

def done(input):
    for char in input:
        if char == '-':
            return False
    return True

def flip(input):
    if input[0] == '-':
        start = '+'
    else:
        start = '-'

    if start in input:
        index = input.index(start)
    else:
        index = len(input)

    for i in range(index):
        if input[i] == '+':
            input[i] = '-'
        else:
            input[i] = '+'
@autosolve
@collects
def solve(tokens):
    input = list(tokens.next_token(str))
    count = 0
    while True:
        if done(input):
            return count
        flip(input)
        count += 1
