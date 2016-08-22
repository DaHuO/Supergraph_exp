def convert (jam, base):
    num = 0
    mul = len(jam) - 1
    for i in jam:
        num = num + int(i) * base**mul
        mul = mul - 1
    return num

def isPrime (num):
    for i in range(2, int(num/2) + 1):
        if (i > 100):
            #well, not really, but it's not worth exploring further
            return 1
        if (num % i) == 0:
            return i
    return 1

def fits (coin):
    divs = [];
    for i in range(2, 11):
        noDiv = isPrime(convert(coin, i))
        if (noDiv == 1):
            return 0
        else:
            divs.append(str(noDiv))
    return divs

def next (cur):
    leng = len(cur) - 2
    now = cur[1:-1]
    part = str(bin(convert(now, 2) + 1))[2:]
    after = '1' + '0'*(leng - len(part)) + part + '1'
    return after

def produce (length, many):
    num = '1' + '0'*(length-2)+ '1'
    list1 = [];
    list2 = [];
    
    while (many):
        divs = fits(num)
        if (divs):
            list1.append(num)
            list2.append(divs)
            many = many - 1
        num = next(num)
        if (len(num) > length):
            break
    
    return list1, list2

list1, list2 = produce(32, 500)

g = open('C-large.out', 'w')
g.write('Case #1:\n')

for i in range(0, len(list1)):
    g.write(str(list1[i]) + " " + " ".join(list2[i]) + '\n')

g.close()

