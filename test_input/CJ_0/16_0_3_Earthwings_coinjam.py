'''
Created on 09.04.2016

@author: Dennis Nienhüser <nienhueser@kde.org>
'''

import argparse
import math
import random

def divisor(n):
    if n % 2 == 0 and n > 2: 
        return 2
    abort = min(5000, int(math.sqrt(n)) + 1)
    for i in range(3, abort, 2):
        if n % i == 0:
            return i
    return 1

def coinJam(value):
    values = []
    for base in range(2,11):
        number = int(value, base)
        div = divisor(number)
        if div == 1:
            return []
        values.append(str(div))
    return values

def parse(filename):
    with open(filename) as file:
        numbers = file.readlines()
    return numbers[1:] if len(numbers) > 0 else []

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("j", help="Number of coins to generate", type=int)
    parser.add_argument("N", help="Coin width", type=int)
    args = parser.parse_args()
    
    found = set()
    digits = ['0', '1']
    #random.seed()        
    print('Case #1:')
    while len(found) < args.j:
        value = '1'
        for i in range(args.N-2):
            value += random.choice(digits)
        value += '1'
        if value in found:
            continue
        jam = coinJam(value)
        if len(jam) > 0:
            print('{} {}'.format(value, ' '.join(jam)))
            found.add(value)
            