import math
import itertools

def isPrime(n):
    maxCheck = int(math.sqrt(n)) + 2
    checkList = [2] + [i for i in range(3, maxCheck) if i % 2 != 0]
    for i in checkList:
        if n % i == 0:
            return i
    return True

f = open("C-small-attempt0.in", "r")
output = open("OUTPUT.txt", "w")

numCases = int(f.readline().strip())
length, numAnswers = map(int, f.readline().strip().split())
answers = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
          31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
          179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
          283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
          353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
          419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
          467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
          547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
          607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
          661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
          739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
          811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
          877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013]
notPrimes = []
chars = ['0', '1']
combinations = list(itertools.product(chars, repeat=length - 2))

for candidate in combinations:
    valid = True
    fullString = '1' + ''.join(candidate) + '1'
    curList = [fullString]
    for base in range(2, 11):
        num = int(fullString, base=base)
        if num in primes:
            valid = False
            break
        else:
            factor = isPrime(num)
            if factor == True:
                valid = False
                primes.append(num)
                break
            else:
                curList.append(factor)
    if valid:
        answers.append(curList)
        if len(answers) == numAnswers:
            break

output.write("case #1:\n")
for answer in answers:
    answerStr = ' '.join(map(str, answer))
    output.write(answerStr + "\n")

f.close()
output.close()

