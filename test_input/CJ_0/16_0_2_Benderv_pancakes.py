import itertools

def pancakes(order):
    order = list(order)
    order = [i[0] for i in itertools.groupby(order)]
    if order[-1] == '+':
        order.pop()
    return len(order)

t = int(input())

for i in range(t):
  line = input().strip()
  print("Case #{}: {}".format(i + 1, pancakes(line)))