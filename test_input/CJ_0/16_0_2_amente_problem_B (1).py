import fileinput

out_file = open('outputB_large', 'w');

def solve(n):
    #print n
    if not '-' in n:
       return 0
    elif not '+' in n:
       return 1

    if '-+' in n:
        idx = n.index('-+')+1
        return solve(n[:idx]) + solve(n[idx:]) 
    else:
        return 1 + solve(n[::-1])
    
    

for i,line in enumerate(fileinput.input("B-large.in")):
    if i != 0:
        n = line.strip()
        ans = "Case #%i: "%i + str(solve(n))
        out_file.write(ans + '\n');

out_file.close()