#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def process(num):

    text = input().split(" ")
    text = list(map(str, text))
    
    if len(text)!=2  :
        return

    limba = int(text[0])
    limso = int(text[1])
    st = int(math.pow(2,limba-1) + 1)
    fn = int(math.pow(2,limba))

    out = ""
    a = 0
    lm = len(text)
    if lm>smax_val and lm < smin_val:
        invite = ""
    else:
        text = list(text)
        for x in range(st, fn + 1):
            con = True

            base = str_base(x,2)
            co = str(base)

            if(co[0] == "0" or co[len(co)-1] == "0"):
                continue

            for y in range(2,11):
                sa = base_con(base,y)
                if is_prime(sa):
                    con = False
                    break
            if con:
                print(base)
                a = a + 1
                out += str(base) + " "
                
                for y in range(2,11):
                        sa = base_con(base,y)
                        for tt in range(2,sa,1):
                            if sa % tt == 0:
                                out = out + str(tt)
                                break
                        if y == 10:
                            out = out + "\n"
                        else:
                            out = out + " "
                            
                if(a==limso):        
                    break
            
    

    return "Case #"+ str(num+1) +":\n" +str(out) + "\n"
            
def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number, base)
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def base_con(number,base):
    st = str(number)
    st = st[::-1]
    toplam = 0
    for x in range(0,len(st)):
        toplam = toplam + math.pow(base,x)*int(st[x])
    return int(toplam)

def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


global tmax
global tmin
global smax_val
global smin_val

tmax = 100
tmin = 1
smax_val = 10
smin_val = 1


global metin
metin=""

tnumber = int(input(""))
#print(str(tnumber))
if (tnumber <= tmax) & (tnumber >= tmin):
    for num in range(0,tnumber):
        metin += process(num)


dosya = open("answer.txt", "w")
dosya.write(metin)
dosya.close()
