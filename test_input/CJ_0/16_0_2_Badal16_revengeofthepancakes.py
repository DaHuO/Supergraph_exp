'''
Created on Apr 9, 2016

@author: mac
'''
def replaceallchar(strng):
    s=list(strng)
    for i in range(len(s)):
        if s[i]=='+':
            s[i] = '-'
        else:
            s[i] = '+'
            
    "".join(s)
    return s
    

f = open('/Users/mac/Desktop/B-large.in','r')
fout = open('/Users/mac/Desktop/output','w')
cases = int(f.readline())
casenum = 1
for line in f:
    pancakes = line.strip()
    ans = ''
    count = 0
    while pancakes:
        if pancakes[-1] == '-':
            pancakes = replaceallchar(pancakes)
            count += 1
        ans = ans + pancakes[-1]
        pancakes = pancakes[:-1]
    print >>fout, 'Case #%d:'%(casenum), count
    casenum +=1
    
