fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

tests_count = int(fin.readline())

def solve():
    s = fin.readline()[:-1]
    prev = ''
    count = 0
    for c in list(s):
        count += (c != prev)
        prev = c
    if s[-1] == '+':
        count -= 1
    return count
    

for test in range(1, tests_count + 1):
    answer = solve()
    fout.write("Case #{}: {}\n".format(test, answer))
