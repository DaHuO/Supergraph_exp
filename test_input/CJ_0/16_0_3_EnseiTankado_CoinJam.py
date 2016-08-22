import math
divisors = ""

divisors = []
answer = []
def is_prime(numb, divis):
    for x in range(2,int(math.sqrt(numb)) + 1):
        if(numb % x == 0):
            divis.append(str(x))
            return False
    return True
    

def check_number(intbina, bina, divisors, answer):
    for i in range(2,11):
        X = 0
        C = intbina
        for j in range(len(bina)):
            X += (C % 10) * (i**j)
            C = int(C/10)
        if( is_prime(X, divisors) == True ):
            return False
    answer.append( "{0} {1}".format(bina, " ".join(divisors)))
    return True
            
    


def main():
    f = open("in.txt", "r")
    T = f.readline()
    N, J = f.readline().split(" ")
    f.close()
    N = int(N)
    J = int(J)
    a = 0
    counter = 0
    fil = open("out.txt", "a")
    fil.write("Case #1:\n")
    fil.close()
    for i in range(2**(N-2)-1):
        divisors = []
        answer = []
        a += 1
        bina = bin(a)
        bina = bina[2:]
        bina = "0"*((N-2)-len(bina)) + bina
        bina = "1" + bina + "1"
        intbina = int(bina)
        if(counter >= J):
            break
        if(check_number(intbina, bina, divisors, answer) == True):
            counter += 1
            print(answer[0])
            fi = open("out.txt", "a")
            fi.write("{0}\n".format(answer[0]))
            fi.close()
            
            
main()


