try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
iput = []

target = open('practise1aout.txt', 'w')



with open('op.txt', 'r') as f:
    iput.append(f.read())

iput = iput[0].split("\n")
numcase=iput[0]
iput = iput[1:len(iput)]


def getLastWord(word,case):
    lastchar=''
    lastword='0'
    finalword=''
    for x in word:
        if x<lastchar:
            lastword=lastword+x
        elif x>=lastchar and x>=lastword[0]:
            lastword = x+lastword
        else:
            lastword = lastword + x

        lastchar=x
    for x in lastword:
        if x!='0':
            finalword=finalword+x
    print  "Case #"+str(case)+": "+str(finalword)



case=1
for x in iput:

    if case<=numcase:
        getLastWord(x,case)
        case=case+1