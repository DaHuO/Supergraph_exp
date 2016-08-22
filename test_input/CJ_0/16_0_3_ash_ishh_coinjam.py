#coinjam
#ashish

T = int(input())

N,J = input().split(' ')
J = int(J)

start_no = '0'*(int(N)-2)
start_no = '1'+start_no+'1'
start_no = int(start_no,2)


def isprime(i):
    if (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0):
        return False
    else:
        return True

def check_prime_on_base(num,base):
    num = list(map(int,str(num)))
    
    num.reverse()
    k = 0
    summ = 0    
    for j,each in enumerate(num):
        summ += (each * (base ** j))
    return isprime(summ)


nos = [i for i in range(start_no,2147487999)]
test_nos = [int("{0:b}".format(each)) for each in nos]
coinjamtest = [each for each in test_nos if str(each)[0] == '1' and str(each)[-1] == '1']


for basex in range(2,11):
    coinjamtest = [each for each in coinjamtest if check_prime_on_base(each,basex)]


legitmatecoins = coinjamtest[:J]

divisor_lis = []

for eachnum in legitmatecoins:
    lis = []

    def fact(num,base):
        lis = []
        num = list(map(int,str(num)))
    
        num.reverse()
        k = 0
        summ = 0    
        for j,each in enumerate(num):
            summ += (each * (base ** j))
    
        for k in range(2,14):
            lis.append(k)
            if summ%k == 0 :
               return k
               break
    
    for o in range(2,11):
        lis.append(fact(eachnum,o))

    divisor_lis.append(tuple(lis))


print("Case #1 :\n")
for x in range(J):
    print(str(legitmatecoins[x]) ,end= ' ')
    for y in divisor_lis[x]:
            print(str(y),end=" ")
    print('\n')
