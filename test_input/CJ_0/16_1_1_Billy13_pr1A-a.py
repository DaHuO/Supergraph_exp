inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    word=list(((inp.readline()).rstrip()))
    ans=[]
    for w in word:
        if ans==[]:
            ans.append(w)
        else:
            if ord(w)>=ord(ans[0]):
                ans.insert(0,w)
            else:
                ans.append(w)
    ans=''.join(ans)
    out.write("Case #" + str(i+1) + ": " + str(ans) + "\n")