def flip(s):
    l = [c for c in s]
    l.reverse()
    for i in range(len(l)):
        if l[i] == "+":
            l[i] = "-"
        else:
            l[i] = "+"
    return l

def solve(S):
    if all(s == "+" for s in S): return 0
    S =[s for s in S]
    count = 0
    for i in range(len(S)-1):
        if S[i]!= S[i+1]:
            S[:i+1] = flip(S[:i+1])
            count += 1
    if all(s == "-" for s in S): 
        count += 1
    return count

def b():
    T = int(raw_input())
    for t in range(1,T+1):
        S = raw_input()
        print "Case #{}:".format(t), solve(S)

if __name__ == '__main__':
    b()