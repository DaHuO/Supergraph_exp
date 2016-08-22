def pancakes(T, N):
    temp = 0;
    while 1 :
        firstOccP = N.find('+')
        firstOccM = N.find('-')
        if firstOccM == -1:
            print 'Case #'+str(T)+': '+str(temp)
            break;
        temp = temp + 1
        if firstOccP == -1:
            N = N.replace('-','+')
            print 'Case #'+str(T)+': '+str(temp)
            break
        if firstOccM < firstOccP :
            N = N[0:firstOccP][::-1].replace('-','+')+N[firstOccP:len(N)+1]
            #print N
            continue
        else:
            N = N[0:firstOccM][::-1].replace('+','-')+N[firstOccM:len(N)+1]
            #print N
            continue
            
            
               
t = int(input())
for i in range(1, t + 1):
    pancakes(i, str(input()))


