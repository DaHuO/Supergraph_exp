__author__ = 'ThomasRiley'
import pprint as p

def nextPair(r, n):
    ans = []
    for s in r:
        ans.append(s+n)
        ans.append(n+s)

    return ans
with open('input.txt') as f:
    testCases = f.readlines()
    n = testCases[0]
    for i in range(1, int(n)+1):
        s = set()
        word = (testCases[i].strip())
        #print(word+" "+str(2**(len(word)-1)))
        res = []
        res.append(word[0])
        j = 1
        while(len(res)<2**(len(word)-1)):

            res = nextPair(res, word[j])
            j+=1
        res.sort()
        print("Case #"+str(i)+": "+str(res[-1]))