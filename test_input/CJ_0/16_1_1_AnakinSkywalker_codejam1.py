# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import re
alphalist=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

fileopen=open("C:/Users/Pazhni/Downloads/A-large.in",'r')
writefileopen=open("C:/Users/Pazhni/Downloads/A-large.out",'wb')

i=0
for red in fileopen:
    if i >0:
        strlist= re.findall('.',red)
        newstr=strlist[0]
        j=1
        while j<len(strlist):
            #print strlist
            #print alphalist.index(strlist[j]),strlist[j],alphalist.index(newstr[0]),newstr[0]
            if alphalist.index(strlist[j])<(alphalist.index(newstr[0])):
                newstr+=strlist[j]
                
            else:
                newstr=strlist[j]+newstr
            j+=1
        reqstr="Case #"+str(i)+": "+str(newstr)+"\n"
        writefileopen.write(reqstr)
    i+=1
writefileopen.close()
fileopen.close()