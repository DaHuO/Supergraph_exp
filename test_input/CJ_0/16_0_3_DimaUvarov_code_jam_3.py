import math
def next_num(a1 = [],n = 0):
    r = n - 2
    while a1[r] == 1:
        a1[r] = 0
        r -= 1
    a1[r] = 1
    return a1

def generate(string):
    return [sym1+sym2+sym3 for sym1 in string for sym2 in string for sym3 in string if sym1+sym2+sym3 not in sym1*3]

def check_is_prime(a1 = ""):
    print(a1)
    answer = []
    for i in range(2,11):
        cur1 = int(a1, i)
        print(cur1)
        if(divider(cur1) == False):
            answer.append(netriv_div(cur1))
        else:
            return []
    return answer



def netriv_div(a1):
    for i in range(2, a1):
        if(a1 % i == 0):
            return i

def divider(n1):
    i = 2
    j = 0
    while i**2 <= n1 and j != 1:
        if n1%i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


inp= open('in3.txt', 'r')
ii = inp.read().split('\n')
t = int(ii.pop(0))
nj = [[int(y) for y in x.split(" ")] for x in ii]
print(nj)



f = open("output3.txt", "w")

print(check_is_prime("100011"))


for i in range(t):
    f.write("Case #" + str(i+1) + ": ""\n")
    count = 0
    a = [0]*nj[i][0]
    a[0] = 1
    a[nj[i][0]-1] = 1
    while(count != nj[i][1]):
        str_a = ""
        for k in a:
            str_a += str(k)

        cur = check_is_prime(str_a)
        # print(cur)
        if(cur != []):
            str_cur = ""
            for k in cur:
                str_cur += str(k) + " "
            f.write(str_a + " " + str_cur + "\n")
            count += 1
        a = next_num(a, nj[i][0])




inp.close()
f.close()