import sys, math

input_number = None
N = None
J = None

with open(sys.argv[1], 'r') as f:
    input_number = f.readline().rstrip()
    next_line = f.readline()
    N = next_line.split()[0]
    J = int(next_line.split()[1].rstrip())

def get_first_integer(n):
     n = int(n)
     binary = "0"*(n-2)
     binary = "1" + binary + "1"
     return int(binary,2)

def generate_coin_jams(start, quantity):
    jams = dict()
    while len(jams) < quantity:
        binary = bin(start)[2:]
        
        ret = is_coin_jam(binary)
        if ret:
            jams[binary] = ret
            #print ("%d coinjams generated" % (len(jams)))

        start = start + 2

    print("Case #%s:" % (input_number))
    for i, j in jams.items():
        string = i + " " + " ".join(jams[i])
        print(string)
        
def is_coin_jam(binary):
        #print("Testing %s" % (binary))

        alist = []
        isprime = False

        for i in range (2,11):
            number = int (binary, i)
            
            ret = is_prime(number)

            if ret == -1:
                isprime = True
                #print("number %d is prime" % (number))
                break
            else:
                #print("number %d is divisible by %d" % (number, ret))
                alist.append(str(ret))

        if not isprime:
            return alist
        else:
            return 0
    

def is_prime(num):
    
    if num==2:
        return 2

    squareroot = math.ceil(math.sqrt(num))

    lista = range(3,squareroot + 1)

    for i in lista:
        if num%i == 0:
            return i

    return -1

def main ():
    first = get_first_integer(N)
    generate_coin_jams(first, J)
    #print(is_coin_jam('100011'))

if __name__ == "__main__":
    main()
