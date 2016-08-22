f=open('B-large.in', 'r')
i=0
N=[]
for line in f:
    if i==0:
        T=int(line)
    else:
        Buffer=line.split('\n')
        N.append(Buffer[0])
    i=i+1
    R=0
for stack in N:
    R=R+1
    #print stack
    coordinate = stack.rfind('-', 0, len(stack))
    Y=0
    if coordinate==-1:
        if R==1:
            fo=open('output.txt', 'w')
            fo.write('Case #'+str(R)+': '+str(Y)+'\n')
        else:
            fo=open('output.txt', 'a')
            fo.write('Case #'+str(R)+': '+str(Y)+'\n')
        fo.close()
    else:
        while coordinate!=-1:
            Y=Y+1
            str_buff=''
            if (len(stack)-1)==coordinate:
                for spl in stack:
                    if spl =='+':
                        str_buff=str_buff+'-'
                    else:
                        str_buff=str_buff+'+'
                stack=str_buff
            else:
                count=0
                for spl in stack:
                    if spl =='+' and count<=coordinate:
                        str_buff=str_buff+'-'
                    elif spl =='-' and count<=coordinate:
                        str_buff=str_buff+'+'
                    else:
                        str_buff=str_buff+spl
                    count=count+1
                stack=str_buff
            coordinate = stack.rfind('-', 0, len(stack))
        if R==1:
            fo=open('output.txt', 'w')
            fo.write('Case #'+str(R)+': '+str(Y)+'\n')
        else:
            fo=open('output.txt', 'a')
            fo.write('Case #'+str(R)+': '+str(Y)+'\n')
        fo.close()
