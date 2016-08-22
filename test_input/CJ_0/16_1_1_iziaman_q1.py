ansList=list()
srcList=list()
def startword(src,str="",index=0):
    if index==len(src):
       # print(str)
        ansList.append(str)
    else:
        startword(src,str+src[index],index+1)
        startword(src,src[index]+str,index+1)

# def sq(i,sword):
#     wrds=list()
#     startword(sword,"",0,wrds)
#     print(wrds)
'''
def startQ1(i,src):
    startword(src,"",0)
    t=sorted(ansList[:])
    res=t[-1]
    print("Case #{}: {}",i,res)
    ansList=list()
'''


def readFromFile(fileName):
    '''
    with open(fileName, "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    return array
    '''
    return [line.rstrip('\n') for line in open(fileName)]


srcList=readFromFile("A-small-attempt0.in")
srcList=srcList[1:]
for i in range(len(srcList)):
    startword(srcList[i])
    ansList=sorted(ansList)
    print("Case #{}: {}".format(i+1,ansList[-1]))
    ansList=list()