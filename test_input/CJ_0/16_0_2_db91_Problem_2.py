
iput=[]
i=0
line=0
output=[]


def NumberFlips(temp,j):

    temp2=[]


    for x in temp:
        temp2.append("+")
    #storing length of ideal array
    var =len(temp2)

    counter=0
    temp4=[]
    #iterating from 0 to x , 0 to x-1 , 0 to x-2 , etc till 0 to 0
    while(var!=0):

        if (temp==temp2):
            break
        temp3=temp[0:var]

        #print "before temp3"+str(temp3)

        if temp3[var-1]=="+":
            temp4.append("+")
            #print str(temp4)+" temp 4"
            pass

        elif  temp3[var-1]=="-":
            counter=counter+1
            for k in range (0,len(temp3)):
              if temp3[k]=="-":
                temp3[k]='+'
              elif temp3[k] == "+":
                temp3[k] = '-'
        for k1 in range(0,len(temp3)):
            temp[k1]=temp3[k1]

        var=var-1

    print  "Case #"+str(j)+": "+str(counter)


with open('op.txt','r') as f:
    iput.append(f.read())

iput=iput[0].split("\n")
iput=iput[1:len(iput)]

case=1
for x in iput:
    temp = []
    for j in x:
        temp.append(j)
    NumberFlips(temp,case)
    case=case+1





