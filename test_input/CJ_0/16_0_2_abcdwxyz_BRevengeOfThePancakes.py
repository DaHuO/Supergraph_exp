t=eval(input())

for i in range(t):
    s=input()
    s=[x for x in s]
    #print(s)
    flips=0
    done=False
    while not done:
        #if tos=+ :cross over all +s, if a - is found,; flip all +s
        if(s[0]=='+'):
            if len(s)==1:
                done=True
                continue
            for j in range(1,len(s)):
                if s[j]=='-':
                    break
            if j==len(s)-1 and s[j]!='-':
                #print("0")
                done=True
            else: #flip +s
                for z in range(j):
                    s[z]='-'
                flips+=1
                    
        #if tos=- : cross over all +s and -s until u find the last -, flip all(including 1st and last -)
        else:
            for j in range(len(s)-1,-1,-1):
                if s[j]=='-':
                    break
            if j==0:
                s[0]='+'
            else:
                copy=s[0:j+1]
                for z in range(len(copy)):
                    if copy[z]=='+':
                        s[len(copy)-1-z]='-'
                    else:
                        s[len(copy)-1-z]='+'
            flips+=1
        #print(s)
    print("Case #",i+1,": ",flips,sep="")
