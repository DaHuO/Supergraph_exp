def lastword(S):
    l = ''
    for i in S:
        if l is  '':
            l += i

        elif i >= l[0]:
            l = i + l
        else:
             l += i
    return l


f = open("A-large.in", 'r')
f1 = open("output.txt", 'w')
noTestcases = int(f.readline())
input = []
for j in range(noTestcases):
    input.append(f.readline().strip())
print input
for i,s in enumerate(input):
    ans = lastword(s)
    f1.write("Case #" + str(i+1) + ": " + str(ans) + "\n")