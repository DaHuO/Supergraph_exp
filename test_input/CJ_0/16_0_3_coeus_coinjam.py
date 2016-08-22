import fileinput
import math
def ten_to_bin(num):
    out = []
    while num > 0:
        out.append(str(num % 2))
        num = num/2
    out.reverse()
    return "".join(out)

def bin_to_bases(bits):
    out = []
    for i in range(2, 11):
        num = 0
        for idx, bit in enumerate(bits):
            num += int(bit) * i**(len(bits)-1-idx)
        out.append(num)
    return out

def divisor(number):
    for i in range(2, 100):#int(math.sqrt(number))+ 1):
        if number % i == 0:
            return i
    return False

def divisors(numbers):
    out = []
    for num in numbers:
        out.append(divisor(num))
    return out

def solve(n, j):
    template = 1 + 2**(n-1)
    cur_number = template
    while j > 0:
        bits    = ten_to_bin(cur_number)
        numbers = bin_to_bases(bits)
        divs    = divisors(numbers)
        if all(divs) == True:
            print "%s %s" % (bits, " ".join(str(d) for d in divs))
            j -= 1
        cur_number += 2


do_see_first = False
case = 1
for ln in fileinput.input():
    if not do_see_first:
        do_see_first = True
        continue
    data = ln.strip()
    n, j = data.split()
    print "Case #%s:" % case
    solve(int(n),int(j))
    case += 1
