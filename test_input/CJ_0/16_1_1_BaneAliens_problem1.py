#!/usr/bin/python

def myfunc(par1):
    result = par1[0]
    for i in xrange(1, len(par1)):
        if par1[i] >= result[0]:
            result = par1[i] + str(result)
        else:
            result += par1[i]

    return result



def main():
    rounds = int(input())
    for r in xrange(1,rounds + 1):
        s = raw_input()
        print ("Case #" + str(r) + ": " + str(myfunc(s)) )

if __name__== "__main__":
    main()
