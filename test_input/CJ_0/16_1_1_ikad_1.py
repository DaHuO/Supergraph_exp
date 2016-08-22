out = open("""C:\Users\Moulik_Adak\Desktop\out.txt""", "w")
inn = open("""C:\Users\Moulik_Adak\Desktop\A-large.in""", "r")
t = int(inn.readline())
i=1

def fn(i):
    s=str(inn.readline())
    x=''
    for _ in range(len(s)):
        if _==0:
            x+=s[_]
            last = s[_]
            continue
        if s[_]>=last:
            x=s[_]+x
            last=s[_]
        else:
            x=x+s[_]
    out.write("Case #"+str(i)+": "+str(x))
while t:
    fn(i)
    i+=1
    t-=1
inn.close()
out.close()
