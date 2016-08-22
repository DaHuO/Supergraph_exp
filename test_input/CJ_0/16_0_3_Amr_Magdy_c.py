from random import randrange
T = raw_input()
N, J = map(int, raw_input().strip().split())

import math
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, min(int(math.sqrt(n)) + 1, 1000), 2):
        if n % i == 0:
            return i
    return 0

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

min_number = int("1"+"0"*(N-2)+"1", 2)
max_number = int("1"*N, 2)
is_ok = []
done = set()
while len(is_ok) < J:
    rand_number = randrange(min_number, max_number)
    if rand_number in done:
        continue
    else:
        done.add(rand_number)
    binary = toStr(rand_number, 2)
    if binary[0] == "0" or binary[-1] == "0" or len(binary) != N:
        continue
    is_prime_list = [int(binary, 2), int(binary, 3), int(binary, 4), int(binary, 5), int(binary, 6), int(binary, 7),
     int(binary, 8), int(binary, 9), int(binary, 10)]
    temp = []
    for index, num in enumerate(is_prime_list):
        result = is_prime(num)
        if result == 0:
            break
        else:
            temp.append(str(result))
            if index == 8:
                is_ok.append({"number": rand_number, "approve": temp})

print "Case #1:"
for item in is_ok:
    print "{binary} {approval}".format(binary=toStr(item["number"], 2), approval=" ".join(item["approve"]))