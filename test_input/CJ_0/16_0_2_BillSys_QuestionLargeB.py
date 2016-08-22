#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def process(num):

    text = input()

    a = 0
    lm = len(text)
    if lm>smax_val and lm < smin_val:
        invite = ""
    else:
        text = list(text)
        while True:
            con = True
            son = -1
            son2 = -1
            for x in range(len(text)-1,-1,-1):
                if text[x] == "-":
                    son = x
                    con = False
                    break
                
            if con:
                break

            a = a+1
            
            if text[0] == "-":
                text = reflect(text,0,son)
            else:
                for x in range(son,-1,-1):
                    if text[x] == "+":
                        son2 = x
                        break
                text = reflect(text,0,son2)
            
            
        text = "".join(text)
    

    return "Case #"+ str(num+1) +": " +str(a) + "\n"
            
def reflect(text,bas,son):
    text2 = text[bas:son+1]
    text2 = text2[::-1]
    for x in range(0,len(text2)):
        if text2[x] == "+":
            text[x] = '-'
        elif text2[x] == "-":
            text[x] = '+'
    
    return text

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


dosya = open("answer2.txt", "w")
dosya.write(metin)
dosya.close()
