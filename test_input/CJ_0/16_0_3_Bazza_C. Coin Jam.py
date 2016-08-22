#https://code.google.com/codejam/contest/6254486/dashboard#s=p2

import math
primeslist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

flenames = ["test","C-small-attempt1","C-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

def numVal(numIn, base):
    if base == 10:
        return numIn

    outVal = 0
    factor = 0
    while numIn > 0:
        outVal += (numIn % 10) * (base**factor)
        numIn = numIn // 10
        factor += 1
    return outVal

def isprime(numin):  #function to test if a number is prime
    if numin == 2:
        return True
    chkmax = max(int(math.sqrt(numin)),2)
    ctr = 2
    isaprime = True
    while ctr <= chkmax and isaprime:
        if numin%ctr == 0:
            isaprime = False
        else:
            ctr += 1
    return isaprime

def lowestprimefactor(target):              #returns lowest prime factor for a number
    curridx = 0                                   #test to see if known prime is a factor
    currprime = primeslist[curridx]
#    maxtest = int(math.sqrt(target)) + 1
    maxtest = 100
    carryOn = True                               #assumes yes unless proven otherwise
    outLPF = target

    while carryOn and currprime < maxtest:
        if target % currprime == 0:
            outLPF = currprime
            carryOn = False

        if carryOn:
            curridx += 1
            if curridx >= len(primeslist):       #no more known primes
                currprime += 2
                while not isprime(currprime):
                    currprime += 2
                primeslist.append(currprime)     #found the next prime and added to list
            else:
                currprime = primeslist[curridx]

    return outLPF

def dectobin(numin):
    return int(bin(numin)[2:])


for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inN, inJ = [int(finp) for finp in flein.readline().split()]
#            inN = int(flein.readline())
#            inStr = flein.readline()

            outstr = "Case #{}:".format(ctrL + 1)
            print outstr
            fleout.write(outstr + "\n")

            startVal = numVal(10**(inN-1) + 1,2)   #Using binary since faster to test for primality on low bases
            endVal = numVal(int("1" * inN),2)
            currVal = startVal
            numFound = 0

            while currVal <= endVal and numFound < inJ:
                testNum = dectobin(currVal)
                tempList = []
                goOn = True
                ctr = 2
                while ctr <= 10 and goOn:
                    tempNum = numVal(testNum, ctr)
                    tempLPF = lowestprimefactor(tempNum)
#                    print testNum, ctr, tempNum, tempLPF
                    if tempNum == tempLPF or tempLPF == 0:
                        goOn = False
                    else:
                        tempList.append(tempLPF)
                        ctr += 1
                if goOn:
                    numFound += 1
                    tempStr = str(testNum)
                    for num in tempList:
                        tempStr += " " + str(num)

                    print numFound, tempStr
                    fleout.write(tempStr + "\n")

                currVal += 2


            #                outpA = line
            #               outstr = "Case #{}: {}".format(ctrL+1,outpA)


#            print outstr
#            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

