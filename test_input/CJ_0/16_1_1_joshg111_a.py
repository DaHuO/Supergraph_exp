import fileinput
from collections import deque

    
def gen_last_word(s):
    res = ""
    q = deque()
    for c in s:
        if not q:
            q.append(c)
        else:
            if c < q[0]:
                # If c is strictly less than first char then append to back of queue.
                q.append(c)
            
            else:
                q.appendleft(c)
                
    for c in q:
        res += (c)
        
    return res
                
    

f = open('workfile', 'w')

if __name__ == "__main__":
    
    i = 1
    f_i = fileinput.input()
    tests = f_i.next()
    for line in f_i:
        #s = map(int, line.split(' '))
        s = line
        res = gen_last_word(s)
        f.write("Case #" + str(i) + ": " + res)
        i += 1
        
    f.close()
    f_i.close()