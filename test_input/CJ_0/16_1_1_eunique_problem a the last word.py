import sys
sys.setrecursionlimit(1500)
def optimal(letter,element,index):
    if index == len(element)-1:
        if letter < element[index]:
            return element+letter
        elif letter > element[index]:
            return letter+element
        else:
            return letter+element
    else:
        if letter < element[index]:
            return element+letter
        elif letter > element[index]:
            return letter+element
        else:
            return optimal(letter,element,index+1)
            
def solve(string):
    counter = 1
    alllist = []
    while counter<=len(string):
        if counter == 1:
            alllist.append(string[0])
            counter+=1
        else:
            element = alllist[-1] 
            alllist.append(optimal(string[counter-1],str(element),0))
            counter+=1
    return alllist[-1]


inputfile = open("A-large.in","r")
outputfile = open("outputfile.txt","w")
counter=0
for line in inputfile:
    counter+=1
    line.strip()
    if counter == 1:
        pass
    else:
        outputfile.write("Case #"+str(counter-1)+": "+solve(line))

outputfile.close()

