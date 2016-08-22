import math

def begin(fn='a', out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = next(fi).split()
            case = next(fi).split(' ')
            fo.write('Case #1: \n')
            solver(int(case[0]),int(case[1]),fo)

#..............................................................................

def checkC(this):
    for j in range(3,10000):
        if this%j == 0:
            return [True,j]
    else:
        return [False]

def solver(ln,x,fo):
    num='1' + '0'*(ln-2) + '1'
    count=0
    while(count<x):
        #print num
        outline=[]
        for base in range(2,11):
            this = int(num,base)
            #print "    ",this
            result=checkC(this)
            if result[0]:
                outline.append(result[1])
            else:
                break
            #print outline
        if len(outline)==9:
            fo.write(num+" ")
            count+=1
            for k in outline:
                fo.write(str(k)+' ')
            fo.write('\n')
        num=bin(int(num,2)+2)[2:]


begin('a')
