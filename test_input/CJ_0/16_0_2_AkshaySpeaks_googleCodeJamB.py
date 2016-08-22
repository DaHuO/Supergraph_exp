tests=int(input())
for test in range(1,tests+1):
    pancakes=input()
    expected='+'
    panSize=len(pancakes)
    ans=0
    for it in range(1,panSize+1):
        if pancakes[-it] is expected:
            continue
        if(expected=='+'):
            expected='-'
        else:
            expected='+'
        ans+=1
    print("Case #",test,": ",ans,sep='')
