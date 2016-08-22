def solve_pancake(lst):
    n = len(lst)
    k = 0

    while sum(lst) != n:
        k += 1

        if sum(lst) == 0:
            return k

        for i in range(n):
            if lst[i] != lst[0]:
                break

        # Inversion
        lst_side = lst[:]
        for j in range(i):
            lst[j] = 1 - lst_side[i - j - 1]

    return k


nb_cases = int(input())

for i in range(nb_cases):
    pancakes = [0 if x == '-' else 1 for x in raw_input()]
    rv = solve_pancake(pancakes)
    print("Case #{}: {}".format(i + 1, rv))
