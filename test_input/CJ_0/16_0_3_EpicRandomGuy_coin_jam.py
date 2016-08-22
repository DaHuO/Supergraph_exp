import random
from sympy import isprime

def main():
    random.seed()

    with file("C-large.in", 'r') as ifs:
        cases = 0
        digits = 0
        examples = 0
        c = int(ifs.read(1))
        ifs.read(1)
        d = int(ifs.read(2))
        ifs.read(1)
        e = int(ifs.read(3))


        cases = c

        for i in range(0, cases):
            print "Case #{}:".format(i+1)

            digits = d

            examples = e

            for j in range(0, examples):
                print jamcoin(digits)



def jamcoin(digits):
    jam = 0
    jam_list = []
    jam_string = ""

    for i in range(0, digits):
        jam_list += str(random.randint(0,1))

    jam_list[0] = '1'
    jam_list[len(jam_list)-1] = '1'

    for i in jam_list:
        jam_string += i


    jam = int(jam_string)
    convert = jam
    temp = []
    result = 0
    divisors = []

    for base in range(2,11):
        for i in range(0, len(str(jam))):
            convert = int(str(jam)[len(str(jam))-i-1])
            convert = convert * base**i
            temp.insert(0, convert)


        for i in temp:
            result += i

        if(isprime(result)):
            return jamcoin(digits) #If test fails try again

        for i in range(2, 300000):
            if(result % i == 0):
                divisors.append(i)
                break
            if(i == 300000-1):
                return jamcoin(digits)

        #divisors.append(result)    
        convert = jam
        temp = []
        result = 0

    jam = str(jam)    

    for i in divisors:
        jam += " " + str(i)



    return jam #If test succeeds return


main()
