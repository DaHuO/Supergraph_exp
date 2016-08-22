import random

f = open('C-large.out', 'w')

N = 16
J = 500

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:        
            return i
    else:
        return None 

numbers = set()

while True:
    s = '1'
    for i in range(N - 2):
        s += str(random.randint(0, 1))
    s += '1'

    lst = []
    for i in range(2, 11):
        k = int(s, i)
 
        p = is_prime(k)
        if p == None:
            lst = []
            break
        else:
            lst.append(str(p))

    if lst != []:
        numbers.add(s + s + " " + " ".join(lst))        
        print(len(numbers))
    else:
        print('fail')
    if len(numbers) == J:
        break
f.write('Case #1:\n')
f.write('\n'.join(list(numbers)))
f.close()
