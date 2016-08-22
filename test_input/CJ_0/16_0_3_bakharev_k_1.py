def toTwo(num):
    result = ""
    while num > 0:
        result += str(int("0") + (num % 2))
        num //= 2
    return result[::-1]

def convert(fromTwo, base):
    number = 0
    fromTwo = fromTwo[::-1]
    for i in range(len(fromTwo)):
        number += (fromTwo[i] == "1") * base ** i 
    return number

def prime(number):
    for i in range(2, 10**5):
        if number % i == 0:
            return i
    return 0

coins = []
div = []
for i in range(2 ** 30 - 1, 0, -1):
    jamcoin = True
    num = 2 ** 31 + i * 2 + 1
    number = toTwo(num)
    divisors = []
    for i in range(2, 11):
        divisor = prime(convert(number, i))
        if divisor == 0 or divisor == num:
            jamcoin = False
            break
        else:
            divisors.append(divisor)
    if jamcoin:
        coins.append(number)
        div.append(divisors)
    
    if len(coins) > 500:
        break

f = open("output.txt", "w")
f.write("Case #1:\n")
for i in range(500):
    f.write(coins[i] + " ")
    for j in range(2, 11):
        f.write(str(div[i][j - 2]) + " ")
    f.write("\n")
f.close()
print(coins)
print(div)