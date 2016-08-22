from __future__ import print_function

import collections
import string
import sys

try:
    input = raw_input
except NameError:
    pass


SWAPPING_TRANS_TABLE = string.maketrans('+-', '-+')


def bfs(starting_state, get_next_states_func, check_func):
    queue = collections.deque([(starting_state, 0)])
    seen_states = set()

    def next_item():
        try:
            return queue.popleft()
        except IndexError:
            return None

    for state, cost in iter(next_item, None):
        new_cost = cost + 1

        for new_state in get_next_states_func(state):
            if new_state not in seen_states:
                item = (new_state, new_cost)

                if check_func(new_state):
                    return item
                else:
                    queue.append(item)
                    seen_states.add(new_state)

    return None


def flip(stack, i):
    new_prefix = stack[:i].translate(SWAPPING_TRANS_TABLE)[::-1]
    new_stack = new_prefix + stack[i:]
    return new_stack


def get_next_states(stack):
    for i in range(1, len(stack) + 1):
        yield flip(stack, i)


def check(stack):
    return set(stack) == {'+'}


if __name__ == '__main__':
    num_cases = input()

    for case_idx, starting_stack in enumerate(iter(sys.stdin.readline, ''), 1):
        starting_stack = starting_stack.strip()

        if check(starting_stack):
            print("Case #{}: 0".format(case_idx))
        else:
            state, cost = bfs(starting_stack, get_next_states, check)
            print("Case #{}: {}".format(case_idx, cost))
