import string

def go():
    f=open('B-large.in')
    c=int(f.readline())
    for case in range(1,c+1):        
        print 'Case #%d:'%case,
        print solve(f.readline().replace('\n',''))
    f.close()

    

def solve(s):
    c=0
    s=list(s)
    #print s
    while '-' in s:
        bot=len(s)-1
        for x in range(bot,-1,-1):
            if s[x]=='-':
                end=x+1
                break
        if  s[0]=='+':
            high=0
            while s[high]=='+' and high<end:
                high+=1
            s=string.join(s,'')
            s=s[0:high].replace('-','t').replace('+','-').replace('t','+')+s[high:]
            s=list(s)
            s[0:high]=reversed(s[0:high])
            c+=1
            #print s

        s=string.join(s,'')
        s=s[0:end].replace('-','t').replace('+','-').replace('t','+')+s[end:]
        s=list(s)
        s[0:end]=reversed(s[0:end])
        c+=1            
        #print s
    return c
    
        
