import math

def convert(s,b):
    x = 0
    for c in s:
        x = int(c) + b * x
    return(x)

def base_list(s):
    lst = []
    b = 1
    while b < 10:
        b += 1
        lst += [convert(s,b)]
    return(lst)

def prime(n):
    maxi = int(math.sqrt(n)) + 1
    for i in range(2,maxi):
        if n%i == 0:
            return(False)
    return(True)

def has_prime_number(lst):
    for x in lst:
        if prime(x):
            return(True)
    return(False)

def smallest_divisor(n):
    for i in range(2,n):
        if n % i == 0:
            return(i)

def list_divisors(lst):
    lst_div = []
    for e in lst:
        lst_div += [smallest_divisor(e)]
    return(lst_div)

def bin(y):
    s = ''
    while y > 0:
        r = y % 2
        y = y // 2
        s = str(r) + s
    return(s)

def jamcoins(N,J):
    x = 1 + 2**(N-1)
    y = x
    i = 0
    file_out.write("Case #1:\n")
    while i < J:
        s = bin(y)
        lst_base = base_list(s)
        k = 0
        if not(has_prime_number(lst_base)):
            k += 1
            file_out.write(s + " ")
            lst_div = list_divisors(lst_base)
            for s in lst_div:
                file_out.write(str(s) + " ")
            file_out.write("\n")
            i += 1
        y += 2
    return(None)

file_in = open("C-small-attempt0.in", "r")
file_out = open("output.out", "w")
T = int(file_in.readline())
N, J = map(int, file_in.readline().split())
jamcoins(N,J)
file_in.close()
file_out.close()