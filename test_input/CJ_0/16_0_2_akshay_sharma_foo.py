n=input()
res_list=[]
for i in range(n):
    s=raw_input()
    res_list.append(list(str(s)))

d=0
for a in res_list:
  
    c=0
    for i in range(len(a)):
        for j in range(i):
            if a[j]!=a[j+1]:
                c=c+1
                for k in range(j+1):
                    a[k]=a[j+1]
    if a[0]=='-':
        for i in range(len(a)):
            a[i]='+'

        c=c+1
    d+=1
    
    

    print 'Case #'+str(d)+": "+str(c)
    
    
        

