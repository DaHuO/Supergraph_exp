from sys import stdin


def read_str(): return stdin.readline().rstrip('\n')
def read_strs(): return stdin.readline().rstrip('\n').split()
def read_int(): return int(stdin.readline())
def read_ints(): return map(int, stdin.readline().split())
def read_floats(): return map(float, stdin.readline().split())


def count_flips(s, happy='+'):
    #print(''.join(s), happy)
    end = len(s) - 1
    while end >= 0 and s[end] == happy:
        end -= 1
    if end < 0:
        return 0
    if end != len(s) - 1:
        s = s[:end + 1]
        
    flips = 0
    begin = 0
    while begin < len(s) and s[begin] == happy:
        begin += 1
    if begin != 0:
        flips = 1
    
    while begin < len(s) and s[begin] != happy:
        begin += 1
    if begin >= len(s):
        return flips + 1
    else:
        s = list(reversed(s[begin:]))
        happy = '-' if happy == '+' else '+'
        return flips + 1 + count_flips(s, happy)
    

def solve_case():
    s = list(read_str())
    return count_flips(s)

    
def main():
    cases = read_int()
    for case in range(1, cases + 1):
        print('Case #{}: {}'.format(case, solve_case()))

        
if __name__ == '__main__':
    main()
