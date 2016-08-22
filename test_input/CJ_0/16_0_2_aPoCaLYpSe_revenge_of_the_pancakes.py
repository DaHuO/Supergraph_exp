import copy
import sys


def parse_case(instrm):
    return instrm.readline().strip()


def solve_case(stack):
    new_stack = stack[0]
    for s in stack[1:]:
        if new_stack[-1] != s:
            new_stack += s
    stack = new_stack
    
    ans = len(stack) - 1
    if stack[-1] == "-":
        ans += 1

    return ans


if __name__ == "__main__":
    instrm = open(sys.argv[1])
    ncases = int(instrm.readline().strip())
    for i in range(ncases):
        case = parse_case(instrm)
        ans = solve_case(case)
        print("Case #{}: {}".format(i+1, ans))
