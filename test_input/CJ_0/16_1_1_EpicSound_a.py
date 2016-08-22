def solve(case):
    poss = [case[0]]
    for l in case[1::]:
        poss0 = [l0+l for l0 in poss]
        poss1 = [l+l0 for l0 in poss]
        poss = poss0
        poss.extend(poss1)
    poss = sorted(poss)
    return poss[-1]
t = int(input())
for i in range(1,t+1):
    case = input()
    print("Case #"+str(i)+": "+"".join(solve(case)))
