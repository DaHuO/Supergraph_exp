def find_div(n):
    d = 2
    while d*d <= n:
        if n%d == 0:
            return d
        d += 1
    return n

input()
N, J = [int(x) for x in input().split()]
print("Case #1:")
for num in range(1+(1<<(N-1)), 1<<N, 2):
    if J == 0:
        break
    sol = []
    s = bin(num)[2:]
    for i in range(2, 11):
        bnum = int(s, i)
        div = find_div(bnum)
        if div == bnum:
            break
        sol.append(str(div))
    if len(sol) is 9:
        print(s, ' '.join(sol))
        J -= 1
