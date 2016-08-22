#! /usr/bin/python3


import sys
print("Case #1: ")
baas = 2147483677

oige = True
leitud = []

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def allyourbasearebelongtous(innitvar, basevar, convertvar):
    innitvar = str(innitvar)
    SY2VA = {'0': 0,
             '1': 1,
             '2': 2,
             '3': 3,
             '4': 4,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             'A': 10,
             'B': 11,
             'C': 12,
             'D': 13,
             'E': 14,
             'F': 15,
             'G': 16,
             'H': 17,
             'I': 18,
             'J': 19,
             'K': 20,
             'L': 21,
             'M': 22,
             'N': 23,
             'O': 24,
             'P': 25,
             'Q': 26,
             'R': 27,
             'S': 28,
             'T': 29,
             'U': 30,
             'V': 31,
             'W': 32,
             'X': 33,
             'Y': 34,
             'Z': 35,
             'a': 36,
             'b': 37,
             'c': 38,
             'd': 39,
             'e': 40,
             'f': 41,
             'g': 42,
             'h': 43,
             'i': 44,
             'j': 45,
             'k': 46,
             'l': 47,
             'm': 48,
             'n': 49,
             'o': 50,
             'p': 51,
             'q': 52,
             'r': 53,
             's': 54,
             't': 55,
             'u': 56,
             'v': 57,
             'w': 58,
             'x': 59,
             'y': 60,
             'z': 61,
             '!': 62,
             '"': 63,
             '#': 64,
             '$': 65,
             '%': 66,
             '&': 67,
             "'": 68,
             '(': 69,
             ')': 70,
             '*': 71,
             '+': 72,
             ',': 73,
             '-': 74,
             '.': 75,
             '/': 76,
             ':': 77,
             ';': 78,
             '<': 79,
             '=': 80,
             '>': 81,
             '?': 82,
             '@': 83,
             '[': 84,
             '\\': 85,
             ']': 86,
             '^': 87,
             '_': 88,
             '`': 89,
             '{': 90,
             '|': 91,
             '}': 92,
             '~': 93}

    integer = 0
    for character in innitvar:
        assert character in SY2VA, 'Found unknown character!'
        value = SY2VA[character]
        assert value < basevar, 'Found digit outside base!'
        integer *= basevar
        integer += value

    VA2SY = dict(map(reversed, SY2VA.items()))

    array = []
    while integer:
        integer, value = divmod(integer, convertvar)
        array.append(VA2SY[value])
    answer = ''.join(reversed(array))

    return answer

from math import sqrt; from itertools import count, islice
def algarv(n):
        for x in range(2, 50):
            if n%x == 0:
                return False
        return True
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
def proof(n):
    leit = False
    i = 2
    while not leit and i < n:
        if n%i == 0:
            leit = True
            return i
        else:
            i += 1
    return "mv"

while len(leitud) < 500:
    if str(baseN(baas,2))[0] == "1" and str(baseN(baas,2))[-1] == "1":
        oige = True
        arv = baseN(baas, 2)
        for j in range(2, 11):
            uusarv = allyourbasearebelongtous(arv, j, 10)
            if isPrime(int(uusarv)) == True:
                oige = False

        if oige == True:
            leitud.append(baas)
            line = ""
            line += baseN(int(baas), 2)
            for k in range(2, 11):
                conv = allyourbasearebelongtous(arv, k, 10)
                line += " "
                line += str(proof(int(conv)))
            print(line)
        baas += 2
    else:
        baas += 2
sys.exit()

