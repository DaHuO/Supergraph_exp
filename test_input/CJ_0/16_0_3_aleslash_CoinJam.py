
#!/usr/bin/python3
import itertools
import random

from sys import argv

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def divisoresNaoComuns(n):
    divisoresComuns = factors(n)
    divisoresComuns.remove(1)
    divisoresComuns.remove(n)
    return divisoresComuns
    
def divisorNaoComum(n):
    listaDivisoresNaoComuns = divisoresNaoComuns(n)
    divisor = listaDivisoresNaoComuns.pop()
    for numero in range(1,random.randint(0,len(listaDivisoresNaoComuns))):
        divisor = listaDivisoresNaoComuns.pop()
    return divisor
   
def frm(x, b):
    """
    Converts given number x, from base 10 to base b 
    x -- the number in base 10
    b -- base to convert
    """
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r
def to(s, b):
    """
    Converts given number s, from base b to base 10
    s -- string representation of number
    b -- base of given number
    """
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    """
    Converts s from base a to base b
    """
    return frm(to(s, a), b)

#for bla in range(2,11):
#    num = convert(str(1001),bla,10) 
#    print  num, isPrime(float(num))
    
#print factors(1001)
#print divisoresNaoComuns(1001)
#print divisorNaoComum(1001)

script, filename = argv

txt = open(filename)

casos = int(txt.readline())

for caso in range(1,casos+1):
    N,J = map(int,txt.readline().strip().split())
    print 'Case #1:'
    #print N,J
    N-=2
    candidatos = []
    for combinacoes in map(''.join,itertools.product(['1','0'],repeat=N)):
        valor = '1'+ combinacoes +'1'
        #print valor
        candidatos.append(valor)
        for base in range(2,11):
            num = convert(valor,base,10) 
            if isPrime(float(num)):
                #print 'dentro', valor
                candidatos.remove(valor)
                break
        if len(candidatos) == J:
            break
    #print candidatos
    impressos = 0
    for candidato in candidatos:
        if impressos == J:
            break
        impressos+=1
        saida = candidato
        for base in range(2,11):
            num = convert(candidato,base,10) 
            saida += ' ' + str(divisorNaoComum(int(num)))
        print saida
        
        
    
        