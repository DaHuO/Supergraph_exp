import numpy as np

testfile='A-large.in'
outputfile='A-large.out'


fo = open(testfile, "rw+")
print "Name of the file: ", fo.name
firstline = fo.readline()

numcases=int(firstline.split('\n')[0])
print 'numcases: ',numcases

def makelastword(firstword):
    print firstword
    args=np.argsort(firstword)
    word=firstword[0]
    firstletter=firstword[0]
    for letter in firstword[1:]:
        if letter>=firstletter:
            word=letter+word
            firstletter=letter
        else:
            word=word+letter
    return word

 

outfile=open(outputfile, 'w')
for case in np.arange(1,numcases+1): 
    print '********'+str(case)+'********'
    firstword=fo.readline()
    answer=makelastword(list(firstword.split('\n')[0]))
    print answer
    outfile.write('Case #'+str(case)+': '+str(answer)+'\n')
    
outfile.close()
fo.close()
b=2
