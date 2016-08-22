flip = {'+':'-', '-':'+'}

def flip_stack(s):
    flip_s = ''
    for c in s:
        flip_s += flip[c]
    return(flip_s)

def flip_string(s):
    n = len(s)
    i = 1
    while i <= n and s[-i] == '+':
        i += 1
    n = n - i + 1
    beg,end = s[:n], s[n:]
    
    c = s[0]
    cnt = 0
    i = 0
    while i < n:
        cnt += 1
        while i < n and beg[i] == c: i += 1
        beg = flip_stack(beg[:i]) + beg[i:]
        c = flip[c]
    s = beg + end
    return(cnt)

file_in = open("B-large.in", "r")
file_out = open("output.out", "w")
N = int(file_in.readline())

cnt = 0
for data in file_in:
    cnt += 1
    s = data.rstrip()
    n_flip = flip_string(s)
    file_out.write("Case #" + str(cnt) + ": " + str(n_flip) + "\n")

file_in.close()
file_out.close()
