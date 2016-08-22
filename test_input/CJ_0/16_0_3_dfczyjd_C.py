def ch(n, k):
    res = 0
    cost = 1
    while n > 0:
        res += (n % 2) * cost
        cost *= k
        n //= 2
    return res


def prime(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            return i
        i += 1
    return 1


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
fin.readlines()
print('Case #1:', file=fout)
n = 16
j = 50
_2n = 2 ** n

for mask in range(_2n // 2 + 1, _2n, 2):
    divs = [0] * 9
    if j == 0:
        break
    for i in range(2, 11):
        ans = prime(ch(mask, i))
        if ans == 1:
            break
        else:
            divs[i - 2] = ans
    else:
        j -= 1
        print(j)
        print(bin(mask)[2:], *divs, file=fout)
fin.close()
fout.close()