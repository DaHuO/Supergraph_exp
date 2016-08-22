import sys

fhIn  = open('input_large', 'r')
fhOut = open('output', 'w') 

nCase = int(fhIn.readline())
for iCase in range(1, nCase+1):

    strHost = list(fhIn.readline())

    listContestant = list([strHost[0]])

    for iPos in range(1, len(strHost)):

        if strHost[iPos] >= listContestant[0]:

            listContestant.insert(0, strHost[iPos])

        else:

            listContestant.append(strHost[iPos])

    strContestant = ''.join(listContestant)


    strResult = format('Case #%d: %s' % (iCase, strContestant))
    print(strResult)

    fhOut.write(strResult)



fhIn.close()
fhOut.close()




