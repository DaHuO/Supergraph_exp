"""Code jam 1A The Last Word."""

import fileinput


def lw(word):
    """Solution."""
    lx = None  # largest letter
    li = None  # largest letter index

    # print(word)

    if len(word) <= 1:
        return word

    for i, x in enumerate(word):
        if lx is None or x >= lx:
            lx = x
            li = i
    return lx + lw(word[:li]) + word[li+1:]

for case, S in enumerate(fileinput.input()):
    if case == 0:
        continue

    print('Case #{}: {}'.format(case, lw(S.strip())))
