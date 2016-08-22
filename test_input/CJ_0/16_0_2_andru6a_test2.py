FILEPATH = "E:\Downloads\B-large.in"

def flip(s):
    res = ""
    for letter in s[::-1]:
        if letter == '+':
            res+=str('-')
        else:
            res+=str('+')
    return res

def pancakes(s):
    count = 0
    char = s[0]
    if len(s) == 0:
        return 0
    while s.find('-') != -1:
        for i in range(0,len(s)):
            if s[i] != char:
                group = flip(s[:i])
                aux = s[i:]
                s = group + aux
                char = s[i]
                count += 1
        if s.find('-') != -1:
            count+=1
            s = flip(s[:])
    return count

def solve(filepath = ""):
    nr = -1
    if filepath == "" or filepath == None:
        filepath = FILEPATH
    with open(filepath) as f:
        for line in f:
            if nr == -1:
                nr = 1
                continue
            result = pancakes(line.strip())
            print ("Case #"+str(nr)+": "+str(result))
            nr += 1
