import re

def printAnswer(caseIndex, answer):
    print("Case #", caseIndex+1, ": ", answer, sep='')

T = int(input())
for t in range(T):
    s = input()
    s = re.sub(r'(.)\1+', r'\1', s)
    if s[-1] == '+':
        s = s[:-1]
    printAnswer(t, len(s))
