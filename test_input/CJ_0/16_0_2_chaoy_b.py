

def run(a):
    n = len(a)
    flip = 0
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            flip += 1
    if a[-1] == '-':
        flip += 1
    return flip

if __name__ == '__main__':
    for t in range(int(input())):
        result = run(input())
        print('Case #{}: {}'.format(t + 1, result))
                       
