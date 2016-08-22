t = int(input().strip())
for at in range(t):
    pancakes = list(input().strip())
    count = 0
    for j in range(len(pancakes) - 1):
        if pancakes[j] != pancakes[j + 1]:
            count += 1
    if pancakes[-1] == '-':
        count += 1
    print('Case #{1}: {0}'.format(count, at + 1))
