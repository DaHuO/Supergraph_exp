t = int(input())

i = 1

def revenge(pancakes):
    count = 1
    prev = pancakes.pop(0)
    while len(pancakes) > 0:
        next = pancakes.pop(0)
        if prev != next:
            count += 1
        prev = next
    if prev == '+':
        count -= 1
    return count

while i <= t:
    pancakes = raw_input()
    print("Case #%d: %d" % (i, revenge(list(pancakes))))
    i += 1
