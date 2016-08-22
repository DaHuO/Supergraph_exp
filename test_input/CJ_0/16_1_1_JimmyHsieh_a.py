def solve(S):
    lastword = ''
    for s in S:
        if (len(lastword) == 0):
            lastword += s
        else:
            if (s < lastword[0]):
                lastword += s
            else:
                lastword = s + lastword
    return lastword            
    
if __name__ == "__main__":
    t = int(input()) 
    for i in range(1, t + 1):        
        n = input()          
        print("Case #{}: {}".format(i, solve(n)))
        
