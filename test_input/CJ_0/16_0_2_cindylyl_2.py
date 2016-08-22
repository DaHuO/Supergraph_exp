case=[]
with open('/Users/cindy_liao/Downloads/B-large.in','r') as file1:
    case_num=file1.readline()
    case=file1.readlines()
for i in range(int(case_num)):
    case[i]=case[i].strip()

def pancake(p):
    count=0
    n=0
    while True:
        num=0
        a=''
        for i in p:
            if i=='+':
                num+=1
        if num==len(p):
            return count
        for j in range(len(p)-1,-1,-1):
            if p[j]=='-':
                n=j
                break

        for k in range(n+1):
            if p[k]=='+':
                a+='-'
            else:
                a+='+'
        p=a+p[n+1:]
        count+=1

for i in range(len(case)):
    with open('/Users/cindy_liao/Desktop/1.txt','a') as file2:
        file2.write('Case #'+str(i+1)+': '+str(pancake(case[i]))+'\n')


