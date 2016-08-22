import itertools


def flip(stack, num):
    copy = [i for i in itertools.islice(stack, 0, num)]
    copy.reverse()
    for x in xrange(len(copy)):

        if copy[x] == '-':
            stack[x] = '+'
        else:
            stack[x] = '-'


def flip_top(stack):
    direction = stack[0]
    num = count_top(stack, direction)
    flip(stack, num)


def count_top(stack, direction):
    return len([i for i in itertools.takewhile(lambda x: x == direction, stack)])


def count_bottom(stack, direction):
    new_stack = [i for i in stack]
    new_stack.reverse()
    return count_top(new_stack, direction)


def is_face_up(stack):
    return len([i for i in stack if i == '-']) == 0


def do_flip(stack, depth=0):
    if is_face_up(stack):
        return depth

    if stack[0] == '+':
        flip_top(stack)
    else:
        flip(stack, len(stack) - count_bottom(stack, '+'))
    return do_flip(stack, depth+1)

