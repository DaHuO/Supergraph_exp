#https://code.google.com/codejam/contest/6254486/dashboard#s=p1

flenames = ["test","B-small-attempt0","B-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

#           inR, inC, inW = [int(finp) for finp in flein.readline().split()]
#           inN = int(flein.readline())
            inStr = flein.readline()

            testStr = inStr
            lenTestStr = len(testStr)
            flips = 0

            while lenTestStr > 0 and "-" in testStr:

#               print testStr, flips

                while lenTestStr > 0 and testStr[-1] == "+":  #Bottom pancakes ok already
                    testStr = testStr[:-1]                    #Remove bottom from stack under consideration

                lenTestStr = len(testStr)

                if lenTestStr > 0:                            #All done?

                    if testStr[0] == "+":  #NOT ready to go to bottom
                        idx = 1
                        while idx < lenTestStr and testStr[idx] == "+":
                            idx += 1

                        testStr = "-" * idx + testStr[idx:]  #Flip the first stack of all +'s
                        flips += 1

                    idx = 1
                    while idx < lenTestStr and testStr[idx] == "-":
                        idx += 1

                    testStr = "+" * idx + testStr[idx:]  # Flip the first stack of all +'s
                    flips += 1


            outpA = flips

            outstr = "Case #{}: {}".format(ctrL+1,outpA)

            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

