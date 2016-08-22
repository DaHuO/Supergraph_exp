def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def getDivisor(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return i

    return -1

def baseConverter(n,base):
    str_num = str(n)
    ans = 0
    for i in range(0,len(str_num)):
        char_int = int(str_num[i:i+1])

        ans += char_int*(base**(15-i))
        # print ans

    return ans

base = (1<<15) + 1
# print(base)
sum = 0
for i in range(1,15):
    sum+=(1<<i)

# print(sum)
low = (1<<1)
#high = 2^1+2^2...2^14
high = sum
#
# print(bin(low+high+base-2)[2:])
#
# print(low+high+base-2)
counter = 0


print(low+high+base-1)
print('Case #1:')
for i in range(low+base-2,low+high+base-1):
    binary = bin(i)[2:]
    if binary[-1]=='0':
        continue

    if counter==50:
        break
    if isPrime(i):
        continue
    else:
        print(bin(i)[2:]),
        counter+=1
        # print(getDivisor(i)),
        for j in range(2,11):
            in_base_j = baseConverter(bin(i)[2:],j)
            # print(in_base_j)
            div = getDivisor(in_base_j)
            print(div),
            if div==-1:
                counter -= 1

        print('')

        # find divisors in all bases







