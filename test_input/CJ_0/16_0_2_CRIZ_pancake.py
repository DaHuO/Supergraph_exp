__author__ = 'Christin'

with open('B-large.in') as f:
    contents = f.readlines()

ans = []
contents = contents[1:]
for d in contents:
    prev = ''
    flag = 0
    #print(len(d))
    if d[0] == '-':
        flag = 1

    count = 0
    i = 0
    while i<len(d):
        if d[i] == '-' and prev == '+':
            count+=2
            i+=1
            while d[i]=='-':
                i+=1
            prev = '+'
            continue
        if d[i] == '+' and prev == '-':
            count+=1
            i+=1
            while d[i]=='+':
                i += 1
            prev = '+'
            continue
        prev = d[i]
        i+=1

    if flag == 1 and count == 0:
        count = 1

    ans.append(count)

count = 1
for d in ans:
    print("Case #"+str(count)+": "+str(d))
    count+=1





