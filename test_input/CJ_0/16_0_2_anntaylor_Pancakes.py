import sys

data = sys.stdin.readlines()
numCases = int(data[0])
cases = data[1:]

def flip(arr):
    arr = [not val for val in arr]
    return arr[::-1]

def check(stack):
    if len(stack) == 1:
        stack = flip(stack)
    for i in range(1,len(stack)):
        if stack[i] != stack[i-1]:
            stack[:i] = flip(stack[:i])
            break
        if i == len(stack)-1:
            stack = flip(stack)
    return stack 

for case in range(len(cases)):
    pancakes = cases[case].rstrip()
    #print(pancakes)
    pancakes = [face == '+' for face in pancakes]
    count = 0
    index = len(pancakes)
    while pancakes[index-1] and index > 0:
        index -= 1
    notHappy = []
    if index == len(pancakes):
        notHappy = pancakes
    else:
        notHappy = pancakes[:index]
    while not all(notHappy):
        notHappy = check(notHappy)
        count += 1
    print("Case #%i: %i" % (case+1, count))
