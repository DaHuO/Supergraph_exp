def find_answer(lst):
    if len(lst) < 2:
        sign_changes = 0
    else:
        sign_changes = sum(p1 != p2 for p1, p2 in zip(lst[:-1], lst[1:]))
    return sign_changes + (lst[-1] == '-')


if __name__ == '__main__':
    n = int(raw_input())
    test_cases = [list(raw_input()) for _ in range(n)]
    for i, tc in enumerate(test_cases):
        print 'Case #{}: {}'.format(i+1, find_answer(tc))