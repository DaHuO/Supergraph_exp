import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



testfile='C-small-attempt1.in'
outputfile='C-small-attempt1.out'

fo = open(testfile, "rw+")
print "Name of the file: ", fo.name
firstline = fo.readline()

numcases=int(firstline.split('\n')[0])

bases=np.arange(2,11)

def jamcointostr(jamcoin):
    return ''.join(map(str,jamcoin))
def jamcointodec(jamcoin):
    exps=np.flipud(np.arange(len(jamcoin)))
    return np.sum(2**exps*jamcoin)
def dectojamcoin(decval):
    return np.array(map(int,list(bin(decval)[2:])))    
primelist=np.array([2,3,5,7,9,11,13,17,19,23,29,31,37])
primelist=np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
def checkjamcoin(jamcoin):
    exps=np.flipud(np.arange(len(jamcoin)))
    values=[np.sum(base**exps*jamcoin) for base in bases]
    divisor=np.arange(len(values))*0
    for i,val in enumerate(values):
        #val/np.arange(2, val)
        #np.mod(float(val)/np.arange(2, val),1)
        args=np.argwhere(np.mod(float(val)/primelist,1)==0)
        if np.shape(args)[0]==0:
            return 0 #not jamcoin
        else:
            divisor[i]=primelist[args[0][0]]
    return divisor




def jamcoins(N,J):
    exps=np.flipud(np.arange(N))
    jamcoin1=np.arange(N)*0
    jamcoin1[0]=1
    jamcoin1[-1]=1
    
    jamcoin2=np.arange(N)*0+1
    
    #testcoinvals=np.arange(jamcointodec(jamcoin1),jamcointodec(jamcoin2)+1)
    #testcoinval=jamcointodec(jamcoin1)
    outstr=''
    count=0
    trys=0
    while count<J:
        jamcoin=jamcoin1
        trys=trys+1
        trysbin=bin(trys)[2:]
        #print trys, bin(trys)[2:]
        if trysbin[-1]=='1': 
            #print 'ok try',trys, bin(trys)[2:]
            trylist=map(int,list(trysbin))
            jamcoin[1:len(trylist)+1]=trylist
          
            #print trys
            #jamcoin=dectojamcoin(testcoinval)
            #if jamcoin[-1]==0: continue
            #print testcoinval,jamcoin
            divs=checkjamcoin(jamcoin)
            if np.any(divs==0)==False :
                count=count+1
                print count
                outstr=outstr+jamcointostr(jamcoin)+' '+' '.join(map(str,divs))+'\n'
        if count==J: break    
    print 'trys',trys,'count',count
    return outstr


outfile=open(outputfile, 'w')
for case in np.arange(1,numcases+1): 
    print '********'+str(case)+'********'
    [N,J]=map(int,fo.readline().split(' '))
    answer=jamcoins(N,J)
    print answer
    outfile.write('Case #'+str(case)+': \n')
    outfile.write(answer)
    
outfile.close()
fo.close()
b=2
