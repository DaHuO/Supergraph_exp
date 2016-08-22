# Pancakes

T = int(input())
for t in range(1, T + 1):
    cakes = input()
    n = 0
    prev = cakes[0]
    for cake in cakes[1:]:
        if cake != prev:
            n = n + 1
            prev = cake
    if prev == '-':
        n = n + 1
    print('Case #%i:' % t, n)