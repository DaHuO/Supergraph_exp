#!/usr/bin/env python3


def from_string(string):
    return list(map(lambda x: True if x == "+" else False, string[::-1]))


def do_flip(stack, count=0):
    if all(stack):
        return count
    flip = []
    cseq = stack[-1:]
    while stack[-1:] == cseq:
        flip.append(stack.pop())
    flip = map(lambda x: not x, flip)
    stack.extend(flip)
    return do_flip(stack, count+1)


if __name__ == '__main__':
    with open("input", "r") as input_file, open("output", "w") as output_file:
        next(input_file)
        case = 1
        for stack_string in input_file.readlines():
            output_file.write("Case #{0}: {1}\n".format(case, do_flip(from_string(stack_string.rstrip()))))
            case += 1
