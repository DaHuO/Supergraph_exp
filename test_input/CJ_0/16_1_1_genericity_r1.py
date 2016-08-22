import math

def readinput():
    inputs=[]
    f=open('input.txt','r')
    for line in f:
        #inputs=line.rstrip().split(' ')
        inputs.append(line.rstrip())
    f.close()
    return inputs
    
def solve(message):
    m=list(message)
    a=[]
    a.append(m[0])
    for i in range(1,len(m)):
        if ord(m[i])>=ord(a[0]):
            a.insert(0,m[i])
        else:
            a.append(m[i])
    return ''.join(a)

inputs=readinput()
inputs=inputs[1:]

f=open('output.txt','w')
for i in range(len(inputs)):
    message=inputs[i]
    f.write('Case #{0}: {1}'.format(i+1,solve(message)))
    f.write('\n')
f.close()