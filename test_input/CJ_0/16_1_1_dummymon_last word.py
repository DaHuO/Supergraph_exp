def outp(a,b):
    file=open("output.txt","a")
    s="Case #"+str(a+1)+": "+str(b)+"\n"
    file.write(s)
    file.close
    print(s)

q=open ("output.txt","w")
q.close()
inp = open("A-large.in","r")
a= []
for line in inp:
    if "\n" in line:
        a.append(line[0:-1])
    else:
        a.append(line)
inp.close()
inpNum =int(a.pop(0))
for case in range(inpNum):
    S = a[case]
    sar = [i for i in S]
    word = []
    for i in sar:
        if len(word) == 0:
            word.append(i)
            continue
        if i >= word[0]:
            word.insert(0,i)
            continue
        word.append(i)
    wordd = ""
    for i in word:
        wordd += i
    outp(case, wordd)
