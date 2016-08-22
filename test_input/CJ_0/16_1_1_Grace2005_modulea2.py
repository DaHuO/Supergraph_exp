#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      lihua
#
# Created:     08/04/2016
# Copyright:   (c) lihua 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

fr=open("C:\Users\lihua\Desktop\Google_Jam\Rd1a\A-large.in","r")
wr=open("C:\Users\lihua\Desktop\Google_Jam\Rd1a\A-large.out","w")


arraylines=fr.readlines()
case=int(arraylines[0])
for i in range(1,case+1):
    a=list(arraylines[i])
    n=len(a)
    b=[' ' for k in range(n)]

    for j in range(0,n):
        if a[j]<b[0]:
            b[j]=a[j]
        else:
            b.insert(0,a[j])
    re=''.join(b)
    print re



    result="Case #"+str(i)+": "+re+"\n"
    wr.write(result)

fr.close()
wr.close()
