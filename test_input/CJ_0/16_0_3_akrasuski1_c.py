import subprocess, sys

def get_factor(n):
    for i in xrange(2,100):
        if n%i==0:
            return i

T=int(raw_input())
N=int(raw_input())
J=int(raw_input())

print "Case #1:"
cnt=0
for curnum in xrange(2**(N-2)):
    num=2**(N-1)+curnum*2+1
    r=bin(num)[2:]
    proofs=[]
    for base in range(2,11):
        num=int(r, base)
        fac=get_factor(num)
        if fac:
            proofs.append(fac)
        else:
            break
    if len(proofs)==9:
        print r,
        for proof in proofs:
            print proof,
        print ""
        cnt+=1
    if cnt>=J:
        break
