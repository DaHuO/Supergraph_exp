class Stack(object):

    stack = ""
    movements = 0
    count = 0
    
    def __init__(self,stack,movements):
        self.stack = stack
        self.movements = movements
        self.count = self.calculateCount()    

    def calculateCount(self):
        number = 0
        for c in self.stack:
            number*=2
            if c == '-':
                number+=1
        return number
                
    
    def flip(self,n):
        newStack = ""    
        for c in self.stack:
            if n>0:
                newp = ''
                if c == '-':
                    newp = '+'
                else:
                    newp = '-'
                newStack = newp+newStack
                n-=1
            else:
                newStack+=c
        return Stack(newStack,self.movements+1)
    
    def __str__(self, *args, **kwargs):
        return self.stack+"("+str(self.movements)+")"
    
    def __repr__(self):
        return str(self)

f = open('B-small-attempt0.in','r')
f2 = open('B-small-attempt0.out','w')

num = 0
for line in f:
    if num == 0:
        num+=1
        continue
    known = [False]*(2**len(line))
    pending = []
    current = Stack(line,0)
    while current.count != 0:
        for i in range(len(current.stack)):
            flipped = current.flip(i+1)
            if not known[flipped.count]:
                known[flipped.count] = True
                pending.append(flipped)
        current = pending.pop(0)
    f2.write("Case #{0}: {1}\n".format(num,current.movements))
    num+=1
f.close()
f2.close()

    



