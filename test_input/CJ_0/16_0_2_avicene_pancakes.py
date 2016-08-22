__author__ = 'adilmezghouti'

def flipper(stack):
    counter = 0
    while True:
        last_position = stack.rfind('-')
        if last_position == -1:
            return counter

        counter += 1
        for i in range(0,last_position + 1):
            if stack[i] == '-':
                new_state = "+"
            else:
                new_state = "-"
            stack = stack[:i] + new_state + stack[i+1:]

with open("input.txt","r") as f:
    cases = f.readline()

    for i in range(0,int(cases),1):
        stack = f.readline()
        print ("Case #" + str(i+1) + ": " + str(flipper(stack)))