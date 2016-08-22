import itertools

digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert (len(digits) == 16)


def asBase(base):
    ret = 0
    for idx, digit in enumerate(digits):
        ret += base ** idx * digit
    return ret


def getAllBasedNums():
    ret = []
    for i in [ii for ii in range(11)][2:]:
        ret.append(asBase(i))
    return ret


def isprime(n):
    if n < 2:
        return True
    if n == 2:
        return True
    if not n & 1:
        return 2
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return x
    return True


numss = []
for posibility in itertools.product(range(2), repeat=14):
    digits = list(posibility)
    digits.insert(0, 1)
    digits.append(1)
    # digits = tuple(1) + posibility + tuple(1)
    numss.append(getAllBasedNums())

results = []
needs = 50
for nums in numss:
    if needs == 0:
        break
    taget = nums[-1]
    evens = []
    for num in nums:
        even = isprime(num)
        if even == True:
            break
        evens.append(even)
    else:
        evens.insert(0, taget)
        results.append(" ".join([str(e) for e in evens]))
        needs -= 1

print(repr(results))

fo = open("3.out", 'w', encoding="UTF-8")
fo.write("Case #1:\n")
for result in results:
    fo.write(result+"\n")