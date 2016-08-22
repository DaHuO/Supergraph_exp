import re
#import time
#start_timer = time.time()
file=open("B.in","r")
filer=file.read()
fr=re.split("\n",filer)
#print(fr)
file.close()
fw=open("B-out.txt","w")
t=int(fr[0])
counter=1
output=""
for i in range(1,(t+1)):
        # Each new case begins
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        st=fr[counter]
        #print("before    "+st)
        st=re.sub(r"\++","+",st)
        st=re.sub(r"\-+","-",st)
        #print("inter    "+st)
        #st=re.sub("a+","a",st)
        #st=re.sub("b+","b",st)
        #st=list(st)
        flip=0
        minus_count=st.count('-')*2
        if st[0]=='+':
                if(len(st)>=2):
                        flip=minus_count
        else:
                flip=minus_count-1
        #print("after   "+st)
        #print(flip)
        counter=counter+1
        
        output=output+"Case #"+str(i)+": "+str(flip)+"\n"
fw.write(output)
fw.close()
#stop_timer = time.time()
#print(stop_timer-start_timer)
                

                
