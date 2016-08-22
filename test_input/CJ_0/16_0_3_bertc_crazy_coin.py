# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 23:28:55 2016

@author: BCLAES
"""
from random import choice
checked_coins = []

def generate_coin(length):
    strout = "1"
    for i in xrange(0,length-2):
        strout += choice(("0","1"))
    strout += "1"
    if strout in checked_coins:
        strrev = strout[::-1]
        if not strrev in checked_coins:
            checked_coins.append(strrev)
            return strrev       
        else:
            return generate_coin(length)
    checked_coins.append(strout)
    return strout

accepted_coins = []
def check_coin(coin):
    #coin = coin[::-1]
    for b in xrange(2,11): #cover every base
        val = 0
        power = 0
        for j in reversed(coin):      #iterate through each 1/0
            val += int(j)*b**power
            power += 1
        #print val
        base_ok = False
        for x in (2,3,5,7,11,13,17,19):
            if val % x == 0:
                base_ok = True
                break
        if base_ok == False:
            break
    #coin = coin[::-1]
    if base_ok == True: #all bases were OK, this is a good coin
        #print "Coin {} accepted".format(coin)
        accepted_coins.append(coin)
        return True
    else:
        #print "Coin {} NOT accepted".format(coin)
        return False
        
to_find = 500 #50
length = 32 #16

with open("C-large.in","r") as f:
    test_cases = int(f.readline())
    for i in xrange(0,test_cases):
        l, n = f.readline().split()
    if int(l)==length and int(n)==to_find:
        print "Input as promised"
    else:
        length, to_find = int(l), int(n)
        print "Expected different input"


while to_find > 0:
    coin = generate_coin(length)
    if check_coin(coin):
        to_find -= 1


def get_num(coin, base):
    val = 0
    power = 0
    for j in reversed(coin):      #iterate through each 1/0
        val += int(j)*base**power
        power += 1
    return val
    
def getdivider(number):
    for x in (2,3,5,7,11,13,17,19):
            if number % x == 0:
                    return x
                    
with open("output-large.txt", "w") as sol:
    sol.write("Case #1:\n")
    for coin in accepted_coins:
        sol.write(coin)
        for b in xrange(2,11):
            div = getdivider(get_num(coin,b))
            sol.write(" {}".format(div))
        sol.write("\n")