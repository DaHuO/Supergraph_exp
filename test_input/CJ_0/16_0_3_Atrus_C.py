from math import sqrt
from itertools import count, islice
def solve(N, J):
    jc=[]
    found = 0
    potential_jc = list(N * "0")
    potential_jc[-1] = "1"
    potential_jc[0] = "1"

    # Find num
    jc_list_10 = changeBase(potential_jc, 2, 10)
    jc_counting_10 = int("".join(jc_list_10))
    while found < J:
        potential_jc = changeBase(jc_list_10, 10, 2)
        divisors = interpret(potential_jc)
        if divisors != [] and potential_jc not in jc:
            jc.append(potential_jc)
            found +=1
            print("".join(potential_jc) + " " + " ".join(map(str, divisors)))
        jc_counting_10 += 2 #since the first digit must remain unchanged..
        jc_list_10 = list(str(jc_counting_10))




def interpret(binary):
    nt_divisors = []
    for i in range(2,11):
        digits = changeBase(binary, i, 10)
        num = int("".join(digits))
        nt_div = find_divisor(num)
        if  nt_div == None:
            return []
        else :
            nt_divisors.append(nt_div)
    return nt_divisors

def find_divisor(n):
    if n < 2:
        return None
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return number
        if number > 1000:
            return None
    return None

def changeBase(digits, old, new):
    number = 0
    for d in digits:
        number = old * number + int(d)
    digits = []
    while number > 0:
        digits.insert(0, str(number % new))
        number  = number // new
    return digits


if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        data = str(input()).split(" ")
        N = int(data[0])
        J = int(data[1])
        print("Case #%i: " % (case_num))
        solve(N, J)
