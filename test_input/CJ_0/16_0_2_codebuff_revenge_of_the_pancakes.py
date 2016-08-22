# from utilities import nonstd
# std = nonstd.IO(in_file='revenge_of_the_pancakes.in', out_file='revenge_of_the_pancakes.out')
#stdin = nonstd.In(in_file='countingsheep.in')


def get_first_upside_pancake_pos(pancake_stack):
    for i in range(len(pancake_stack)):
        if pancake_stack[i] == '-':
            return i

    return -1


def flip_pancakes(pancake_stack, pos):
    for i in range(pos):
        pancake_stack[i] = '-'


test_cases = int(input())

for test_case in range(test_cases):
    maneuver = 0
    proper_stack = False
    pancake_stack = list(str(input()).strip())
    while not proper_stack:
        if pancake_stack[0] == '+':
            first_upside_pancake_pos = get_first_upside_pancake_pos(pancake_stack)
            if first_upside_pancake_pos == -1:
                proper_stack = True
            else:
                maneuver += 1
                flip_pancakes(pancake_stack, first_upside_pancake_pos)
        elif pancake_stack[0] == '-':
            maneuver += 1
            for i in range(len(pancake_stack)):
                if pancake_stack[i] == '-':
                    pancake_stack[i] = '+'
                elif pancake_stack[i] == '+':
                    break

    print('Case #' + str(test_case+1) + ': ' + str(maneuver))


