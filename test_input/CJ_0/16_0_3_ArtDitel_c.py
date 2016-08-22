


def proof(x):
    for i in range(2, min(1000,x-1)):
        if x % i == 0:
            return i
        i += 1
    return 0

N = 32
J = 500

i = (1 << (N-1))

print ("Case #1:")
while J:
    i += 1
    if i % 2 == 0:
        continue
    if i >= 1  << N:
        break
    s = format(i, 'b')
    proofs = [s]
    for j in range(2,11):
        k = int(s, base=j)
        p = proof(k)
        if p == 0:
            break
        proofs.append(p)
    if len(proofs) == 10:
        J -= 1
        print(*proofs)
