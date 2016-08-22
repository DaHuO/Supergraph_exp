import sys

def flip(c):
    return '+' if c == '-' else '-'

def solve(test_id):
    s = [c for c in input().strip()]
    ans = 0
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1]:
            s[0:i + 1] = s[0:i + 1][::-1] 
            s[0:i + 1] = [flip(s[j]) for j in range(0, i + 1) ]
            ans += 1
    if '-' in s:
        ans += 1
    print('Case #{}: {}'.format(test_id, ans))
    print('Case #{}: {}'.format(test_id, ans), file = sys.stderr)

def main():
    test_cases = int(input().strip())
    for test_id in range(1, test_cases + 1):
        solve(test_id)

if __name__ == '__main__':
    main()
