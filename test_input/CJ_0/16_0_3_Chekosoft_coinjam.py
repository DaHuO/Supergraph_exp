import math

def is_prime(a):
    return all([i % 2 for i in range(2,int(a/2))])

def generate_coinjams(length):
    coinjams = []
    number = 2 ** (length-1)
    while number & 2**(length) == 0:
        if number & 1 == 1:
            coinjams.append(number)
        number += 1

    return map(lambda x: bin(x), coinjams)

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def is_coinjam(candidate):
    for i in range(2, 11):
        sub_candidate = int(candidate[2:], i)
        if is_prime(sub_candidate):
            return False
    return True

def get_nontrivial_divisor(number):
    for i in range(2, number):
        if number % i == 0:
            return i

length, assured = (16, 50)

results = []
for number in generate_coinjams(length):
    if is_coinjam(str(number)):
        results.append(number)
    if len(results) == assured:
        break

with open('output-small.txt', 'w') as output:
    output.write('Case #1:\n')
    for result in results:
        result_str = str(result)[2:]
        output.write(result_str)
        for n in range(2, 11):
            output.write(' ' + str(get_nontrivial_divisor(int(result_str, n))))
        output.write('\n')
