__author__ = 'chamathsilva'


output = ''


def finder(data):
    stack = list(reversed(data))

    state = '+'
    flip_cont = 0
    previous = -99

    for i in range(len(stack)):
        current = stack[i]
        if previous == current:
            continue

        elif state != current:
            if state == '+':
                state = '-'
            else:
                state = '+'

            flip_cont += 1
            previous = current

    return flip_cont


for i in range(int(input())):
    output += "Case #"+str(i+1)+": "+str(finder(input()))+'\n'


print(output)

