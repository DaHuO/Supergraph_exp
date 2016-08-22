import math
def is_prime(n):
    if n % 2 == 0:
        return 2

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return i
    return 1
results= []
primes = []
counter = 0
output = ""
n = 16
j = 50
for k in range(2**(n-1)+1,2**n,2):
    l = bin(k)[2:]
    goOn = True
    base = 2
    result = str(l)
    while goOn:
        prime = is_prime(int(l, base))
        if prime==1:
            goOn = False
        else:
            result += " "
            result += str(prime)
            base += 1
            if base == 11:
                goOn = False
                output += result
                output += "\n"
                counter += 1
                print(counter)
    if counter == j:
        break
    

            



"""output += "Case #" + str(i+1) + ": " + str(counter) + "\n"""


print(output)
