import sys

inp = sys.stdin
inp = open("B-large.in","r")
outp = open("out","w")
#outp = sys.stdout
def read_inp():
    return inp.readline().strip()

mem = {}

def flip(s):
    if s =='+':
        return 0
    if s == '-':
        return 1
    if s in mem:
        return mem[s]
    
    if s[-1] == '+':
        a = flip(s[:-1])
        
    elif s[-1] == '-':
        s2 = ''.join(['+' if ss == '-' else '-' for ss in s]) 
        a = flip(s2[:-1]) + 1
    
    sr = ''.join(reversed(s))
    if sr[-1] == '+':
        b = flip(sr[:-1])
        
    elif sr[-1] == '-':
        s2 = ''.join(['+' if ss == '-' else '-' for ss in sr]) 
        b = flip(s2[:-1]) + 1
    b+=1
    
    mem[s] = min(a,b) 
    return mem[s]
    
    
        
    
T = int(read_inp())

for t in xrange(1,T+1):
    seq = read_inp()
    
    ans = flip(seq)
    outp.write("Case #%d: %s\n"%(t,ans))

outp.close()