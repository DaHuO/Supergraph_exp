__author__ = 'bharath'

def rev(temp):
    res=""
    for i in temp:
        if i=='+':
            res+='-'
        else:
            res+='+'
    return res

def main():
    t=input()
    for i in range(0,t):
        s=raw_input()
        count=0
        j=len(s)-1
        while j>=0:
            while j>=0 and s[j]=='+':
                j-=1
            if j<0:
                break
            correct = s[j+1:]
            temp=s[:j+1]
            s=rev(temp)+correct
            count+=1
        print "Case #%d: "%(i+1)+str(count)
if __name__=="__main__":
    main()