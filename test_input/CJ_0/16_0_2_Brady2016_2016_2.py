import time
import random

oldtime=time.time()
def exchange(str,i):
    oldlist=list(str)
    strnew=oldlist[:]
    for index in range(len(oldlist)):
        if i-index >= 0:
            if oldlist[i-index]=='-':
                strnew[index]='+'
            else:
                strnew[index]='-'
        else:
            break
    return ''.join(strnew);

def letsdo(str):
    "infiniti loop"    
    count=0
    min=999
    leng=len(str)
    while count<1:
        newstr=str[:]
        count=count+1
        inside=0
        while inside<min and newstr.find('-')!=-1:
            inside=inside+1
            '''
            if random.random()>0.5:
                if newstr[0:1]=='-':
                    start=newstr.find('+')-1
                else:
                    start=newstr.find('-')-1
            else:
                if newstr[-1]=='-':
                    start=newstr.rfind('+')
                else:
                    start=newstr.rfind('-')
            '''
            if newstr[0:1]=='-':
                start=newstr.find('+')-1
            else:
                start=newstr.find('-')-1
            
            if start<0:
                break
            if start+1!=leng:
                newstr=exchange(newstr,start)
        if(min>inside):
            min=inside
    return min
            

#print(letsdo('--+-+--+----+-+--+----+-+--+----+-+--+----+-+--+----+-+--+--'))



file = open("a")
T = file.readline()
all_the_text=[]

for num in range(1,int(T)+1):
    final=file.readline().rstrip()
    newfinal=letsdo(final)
    temstr='Case #'+str(num)+': '+str(newfinal)+'\n'
    print(temstr)
    all_the_text.append(temstr)
    
file_object = open('thefile.txt', 'w+')
file_object.writelines(all_the_text)
file_object.close( )

print(time.time()-oldtime)
