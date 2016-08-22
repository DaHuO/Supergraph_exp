import random
file = open("C:\Users\Luca\Downloads\C-small-attempt4.in", "r")
file2 = open("ans.txt", "w")
times = file.readline()

def isprime(n):
    divisors = []
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            divisors.append(x)
        if len(divisors) > 1:
            break

    if divisors == []:
        return True
    else:
        return random.choice(divisors)

def convert(jam, base):
    n_num = 0
    for n in range(0, len(str(jam))):
        n_num += int(str(jam)[len(str(jam)) - n - 1]) * (base ** n)

    return n_num

def check(jam):
    ns = str(jam) + " "
    for base in range(2, 11):
        if isprime(convert(jam, base)) == True:
            return False
        else:
            ns = ns + str(isprime(convert(jam, base))) + " "

    return ns

for time in range(0, int(times)):

    s = "Case #" + str(time + 1) + ":"
    file2.write(s)

    line = file.readline()
    i = line.find(" ")
    lenght = int(line[0:i])
    j = line[2:].rstrip()
    " ".join(j.split())
    j = int(j)

    right_ones = []

    while len(right_ones) < j:
        all = []
        jam = "1"
        for x in range(lenght - 2):
            jam = jam + str(random.randint(0, 1))
        jam = jam + "1"

        if jam in all or not check(jam):
            pass
        else:
            file2.write(check(jam))
            right_ones.append(jam)

        all.append(jam)
        del jam