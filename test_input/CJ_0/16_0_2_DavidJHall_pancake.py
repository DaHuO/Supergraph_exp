import time
trials = 100000000

infilename ='B-large.in'


timestart = time.time()
iterations = 0
problem = []

def flip(singlepancake):
    if singlepancake == '-':
        return '+'
    return '-'

def flipstack( subpancakes):
 #   print "got"+subpancakes
    pancakereturn = ''
   # subpancakes = subpancakes[::-1]
    for i in subpancakes:
        pancakereturn += flip(i)
#    print "returning"+pancakereturn
    return pancakereturn

def checkPerfect(stack):
    for i in range(len(stack),0,-1):
        if stack[i-1]=='-':
            return i
    return -1


def solve(pancakes):
    location = 0
    times = 0
    location=checkPerfect(pancakes)
 #   print "!"+str(location)
    while (location+1):
        times += 1
#        print "not perfect", location
        pancakes = flipstack(pancakes[0:location] ) + pancakes[location:]
        # print "Pancakes"+pancakes

        location=checkPerfect(pancakes)
#    print "perfect"
    return times


f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    # print i
    problem.append( f.readline().strip() )
fw = open('out3.txt', 'w')
num = 1
for i in problem:
    answer=str(solve(i))
    print "Case #"+str(num)+": "+str(answer)
    fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num += 1

#fw = open('out2.txt', 'w')
#print problem
#num = 1
#answer = ''
#for i in problem:
#    answer=str(altsolve(i))
#    print "Case #"+str(num)+": "+answer
# fw.writelines("Case #"+str(num)+": "+answer+"\n")
#    num +=1


print time.time()-timestart





