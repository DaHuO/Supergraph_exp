# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
t = int(stdin.readline())
for ca in xrange(1,t+1):
    a = stdin.readline().strip()
    ans= a[0]
    a = a[1:]
    for i in a:
        if i >= ans[0]:
            ans = i+ans
        else:
            ans = ans+i
    print ("Case #%d: %s")%(ca,ans)