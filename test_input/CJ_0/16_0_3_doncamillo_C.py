from numba import jit


@jit
def is_jamcoin(C):
    divisors = [0] * len(C)
    for i in range(len(C)):
        # there are still over 5000 jamcoins
        for d in range(2, min(int(C[i]**0.5)+1, 100)):
            if C[i] % d == 0:
                divisors[i] = d
                break
        if not 0 < divisors[i]:
            return divisors
    return divisors

with open("C-small-attempt0.in") as casefile:
    casefile.readline()
    N, J = map(int, casefile.readline().strip().split())

print("Case #1:")
for num in range((1 << N-1)+1, (1 << N), 2):
    if not J:
        break
    bin_str = str(bin(num))[2:]

    divisors = is_jamcoin([int(bin_str, b) for b in range(2, 11)])
    if all(divisors):
        print(bin_str, *divisors)
        J -= 1
