import pyprimes

max = 50

i = 0
curr = 0
print "Case #1:"

while (i < max):
    num = "1{0}1".format("{0:014b}".format(curr))
    is_prime = False
    arr = []
    for base_1 in range(9):
        base = base_1 + 2
        if pyprimes.miller_rabin(int(num, base)):
            is_prime = True
            break
        else:
            arr.append(str(pyprimes.factors(int(num, base))[0]))
    if not is_prime:
        print num + ' ' + ' '.join(arr)
        i += 1
    curr += 1
