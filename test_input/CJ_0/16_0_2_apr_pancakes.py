def solve(cakes,tries):
    if cakes == "+"*len(cakes):
        return str(tries)
    fpc = cakes[0]
    i = 1
    while (i < len(cakes) and cakes[i] == fpc):
        i += 1
    flip = "".join(map(lambda x: '+' if x == "-" else "-", reversed(list(cakes[0:i]))))
    cakes = flip + cakes[i:]
    return solve(cakes,tries+1)




f = open('input.txt', 'r')
o = open('output.txt', 'w')
lines = f.readlines()
T = int(lines[0])
for i in range(T):
    ans = "Case #" + str(i+1) + ": " + solve(lines[i+1].strip(),0)
    o.write(ans + "\n")
