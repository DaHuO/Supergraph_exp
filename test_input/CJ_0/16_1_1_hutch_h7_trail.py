

noOfCases = int(raw_input())
output=open('h7_trail_out.txt','w+')
for i in xrange(1,noOfCases+1):
    inpt = raw_input()
    inpt = list(inpt)
    outpt = ''
    li=[]
    li.append(inpt[0])
    for j in inpt[1:]:
        if(j>=li[0]):
          li.insert(0,j)
        else:
          li.append(j)
    output.write("Case #" + str(i) + ": " + ''.join(li) + "\n")
print ''.join(li)