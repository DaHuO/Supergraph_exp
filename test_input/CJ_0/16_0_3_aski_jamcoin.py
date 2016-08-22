import itertools
t = int(raw_input())

def toRemove(item):
    if item[0]=='0' or item[len(item)-1]=='0':
        return True
    else:
        return False

def findBaseEquivalent(num, base):
    rev = num[::-1]
    j=0
    final_num=0
    for i in rev:
        final_num += int(i)*(pow(base,j))
        j+=1
    return final_num

def find_non_trivial_divisor(num):
    for i in xrange(2,num):
        if num%i==0:
            return i

# print find_non_trivial_divisor(findBaseEquivalent('100011',5))

#Optimized prime number
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False
    return True




for i in range(t):
    #Extract Values
    print "Case #"+str(i+1)+': '

    sc_line = raw_input()
    sc_line = sc_line.split(' ')
    N = int(sc_line[0])
    J = int(sc_line[1])
    # print N
    # print J
    generated_items = ["".join(seq) for seq in itertools.product("01", repeat=N)]
    filtered_items = []

    for j in range(len(generated_items)):
        if toRemove(generated_items[j]):
            continue
        else:
            filtered_items.append(generated_items[j])

    del generated_items

    count =0
    for k in xrange(len(filtered_items)):
        jam_coin = False
        # print '-'*6
        # print filtered_items[k]
        # print '-'*6
        non_trivial_list = []
        for l in range(2,11):
            baseEq = findBaseEquivalent(filtered_items[k],l)
            if isPrime(baseEq):
                jam_coin = False
                break
            else:
                # print 'NotPrime'
                non_trivial_list.append(baseEq)
                jam_coin = True

        if jam_coin:
            count +=1
            new_list = []
            # print non_trivial_list
            for m in non_trivial_list:
                last_val = str(find_non_trivial_divisor(m))
                new_list.append(last_val)
            print str(filtered_items[k])+' '+' '.join(new_list)
        if count==J:
            break
