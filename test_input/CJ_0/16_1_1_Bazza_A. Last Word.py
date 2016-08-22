#https://code.google.com/codejam/contest/4304486/dashboard

flenames = ["test","A-small-attempt0","A-large"]  #.in for input .out for output
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

            outputstr = inStr[0]

            for ctr in range(1,len(inStr)):
                if ord(inStr[ctr]) >= ord(outputstr[0]):
                    outputstr = inStr[ctr] + outputstr
                else:
                    outputstr = outputstr + inStr[ctr]


            outpA = outputstr
            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr)


        flein.close()
        fleout.close()

