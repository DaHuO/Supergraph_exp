

for case in range(1,int(input())+1):
    R=list()
    S=list(input())
    for i in S:
        if len(R) == 0:
            R.append(i)
        else:
            if i >= R[0]:
                R.insert(0,i)
            else:
                R.append(i)
    print("Case #"+str(case)+": "+"".join(R))
