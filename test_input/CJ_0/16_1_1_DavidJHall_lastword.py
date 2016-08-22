import time


infilename ='A-small-attempt0.in'

def flipbit(mybit):
    if mybit:
        mybit = False
    else:
        mybit = True
    return mybit


def solve(word):

    possibles = 2**(len(word)-1)
    answers = word[0]
    for i in range(1,len(word)):
        # print word[i]
      #  print "answers" + str(answers)
        temparray=[]
        for j in answers:

            # add left
            temparray.append(word[i]+j)
            # add right
            temparray.append(j+word[i])
     #       print "temp"+str(temparray)
        answers = temparray
    #print answers






    sortedarray =  sorted( answers)

    return sortedarray[len(answers)-1]

timestart = time.time()
iterations = 0
problem = []

f = open(infilename, 'r')
iterations = int(f.readline())
for i in range(0,iterations):
    problem.append( (f.readline().strip()) )




fw = open('out1.txt', 'w')
print problem
num = 1
answer = ''
for i in problem:
    answer=str(solve(i))
    print "Case #"+str(num)+": "+answer
    fw.writelines("Case #"+str(num)+": "+answer+"\n")
    num +=1


print time.time()-timestart





