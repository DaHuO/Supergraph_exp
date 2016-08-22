#!/usr/bin/python
import itertools

class coins:
    def __init__(self,file):
        self.primeset = set()
        with open(file) as primes:
            for i in primes:
                current = int(i.strip())
                self.primeset.add(current)
                if current > 2147483647:
                    break
        print("end")


    def isPrime(self,number):
        return number in self.primeset


def finddevisor(number):
    shortset = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in shortset:
        if number % i == 0:
            return i


#handig = coins("prime.dat")

def checkprimebases(number):
    list = []
    for i in range(2, 11):
        devisor = finddevisor(int(str(number), i))
        if devisor != None:
            list.append(devisor)
        else:
            return False
    return list

def createjam(number,amount):
    count,i = 0,0
    number = number - 2
    print("Case #1:")
    for i in itertools.product("10", repeat=number):
        bases = checkprimebases(int("1"+"".join(i)+"1"))
        if isinstance(bases, list):
            print("{} {} {} {} {} {} {} {} {} {}".format("1"+"".join(i)+"1", bases[0], bases[1], bases[2], bases[3],
                                                         bases[4], bases[5], bases[6], bases[7], bases[8]))
            count += 1
        if count >= amount:
            break

createjam(32,500)

