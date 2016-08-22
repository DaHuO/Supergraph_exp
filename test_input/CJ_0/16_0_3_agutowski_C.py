_ = input()
n, j = map(int, input().split())
print('Case #1:')
for i in range(j):
    x = '11' + ''.join((c*2 for c in bin(i)[2:].rjust((n-4)//2, '0'))) + '11'
    print(x, ' '.join(str(int('11', b)) for b in range(2, 11)))
