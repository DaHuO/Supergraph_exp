
def maneuver_counter(l):
    c=0
    for i in range(0, len(l)):
        for j in range(i):
            if l[j]!=l[j+1]:
                c=c+1
                for k in range(j+1):
                    l[k]=l[j+1]
    if l[0]=='-':
        c=c+1
    return c

x=input()
res_list=[]
for i in range(x):
    i=raw_input()
    res_list.append(maneuver_counter(list(str(i))))
for i in range(0, len(res_list)):
    print "Case #"+str(i+1)+": "+str(res_list[i])  
            
        
             
