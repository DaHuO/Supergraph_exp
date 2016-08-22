
def solve(s: str) -> int:
    count = 0
    while not end_check(s):
        count += 1
        s = flip(s, get_prefix_len(s))
    return count


def flip(s: str, len: int) -> str:
    base = '+' if s[0] == '-' else '-'
    s = base*len + s[len:]
    return s


def get_prefix_len(s: str) -> int:
    count = 0
    base = s[0]
    for ch in s:
        if ch != base:
            break
        count += 1
    return count


def end_check(s: str) -> bool:
    for ch in s:
        if ch != '+':
            return False
    return True


if __name__ == '__main__':

    lines_count = int(input())

    cases = []
    for i in range(lines_count):
        input_ = input()
        cases.append(str(input_))

    for idx, n in enumerate(cases):
        result = solve(n)
        print('Case #%d: %d' % (idx+1, result))