import math
def is_prime(num):
    x = True
    for i in range(2, num):
        if num%i == 0:
            return False
        else:
            x = True

    return x

def first_divisor(num):
    for f in range(2, 2000):
        if num%f == 0:
            return f
    return None

def is_jamcoin(base):
    for k in range(2, 11):
        if is_prime(base[k]):
            return False
        else:
            return True


text_file = open("C-large.in", "r")
lines = text_file.readlines()
que = lines[1]
z1, z2 = que.split(' ')
text_file.close()

N = int(z1)
J = int(z2)

count = 0

n = (10**(N-1))+1
max_n = (10**N)

b = int(str(n), base=2)
max_b = int(str(max_n), base=2)
i2=0
ab = []

for i in range(b, max_b):
    i2+=1
    if int((format(i, 'b')), base=10) % 10 != 0:
        ab.append(int(format(i, 'b'), base=10))
    if i2==5000:
        break
print(ab)
print(len(ab))
a = ab
print(a)
print(len(a))



text_file = open("Output.txt", "a")
text_file.write("Case #1:\n")
text_file.close()
for j in range(len(a)):
    base = []
    divisor = []
    # added these line so base value and the list position value is same.
    base.append(0)
    base.append(0)
    divisor.append(0)
    divisor.append(0)

    for k in range(2, 11):
        base.append(0)
        a2 = a[j]
        for f in range(0, N):
            digit = a2 % 10
            a2 = a2//10
            base[k] += digit * (k ** f)

    print(base)

    for k in range(2, 11):
        divisor.append(0)
        divisor[k] = first_divisor(base[k])
        #print(k)
    print(divisor)

    if not None in divisor:
        text_file = open("Output.txt", "a")
        text_file.write("%s" % a[j])
   #     print(a[j], ' ', end="")
        for f in range(2, 11):
                text_file.write(" %s" % divisor[f])
        text_file.write("\n")
        text_file.close()
        count += 1
        if count == J:
            break
