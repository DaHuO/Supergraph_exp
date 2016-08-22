def sol(s):
    curr = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] != curr:
            curr = s[i]
            count += 1
    if s[-1] == '+':
        return str(count-1)
    else:
        return str(count)



fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    if case > 0:
        print("Case"+str(case))
        fOut.write("Case #"+str(case)+": "+sol(line.strip())+"\n")
    case += 1