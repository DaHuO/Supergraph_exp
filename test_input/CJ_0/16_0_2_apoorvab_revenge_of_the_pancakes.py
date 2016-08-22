__author__ = 'apoorvab'

# Google Code Jam Qualification Round - Revenge of the Pancakes
# Observation: as soon as you get +'s at the end of the stack you can focus on
# everything above it in the stack.
#
# Case 1: all + ==> return 0
# Case 2: all - ==> return 1 (flip once)
# Case 3: + at bottom of stack ==> solve for everything above continuous set of +'s
# Case 4: - at bottom of stack
#   a: - at top of stack, flip entire stack to conver it to case 2
#   b: + at top of stack, solve for -'s and flip entire stack at end


def get_parsed_line():
    return list(input())


def get_case():
    stack = ''.join(get_parsed_line())
    return stack


def get_flip_count(stack):
    if stack == len(stack)*'+':
        return 0
    elif stack == len(stack)*'-':
        return 1
    elif stack[-1] == '+':
        return get_flip_count(stack[0:stack.rfind('-') + 1])
    elif stack[-1] == '-':
        inverted_stack = stack.replace('+', 'x').replace('-', '+').replace('x', '-')
        if stack[0] == '-':
            return get_flip_count(inverted_stack[::-1]) + 1
        else:
            return get_flip_count(inverted_stack) + 1

    return int('DEADBEAF', 16)


if __name__ == '__main__':
    num_cases = list(map(int, input().split()))[0]

    for case_num in range(0, num_cases):
        stack = get_case()
        print('Case #%d: %d' % (case_num + 1, get_flip_count(stack)))
