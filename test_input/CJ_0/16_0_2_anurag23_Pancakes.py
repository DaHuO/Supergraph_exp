def countFlips(n):
    count = 0
    last = ''
    for c in n:
        if last != '-' and c == '-':
            count += 1
        if last == '+' and c == '-':
            count += 1
        last = c
    return str(count)

t = int(input())
for i in range(1, t+1):
    print("Case #{}: {} ".format(i, countFlips(input())))