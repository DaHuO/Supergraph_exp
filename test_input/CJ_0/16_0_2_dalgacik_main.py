session = 'B-large'

filename_in = session + '.in'
filename_out = session + '.out'

def flip(x):
    y = [None]*len(x)
    for i in range(len(x)):
        if x[i] == '+':
            y[-i] = '-'
        else:
            y[-i] = '+'
    
    return y

def check_solved(x):
    for ch in x:
        if ch == '-':
            return False
    return True
    
def detect_tail(x):
    tail = len(x)
    while True:
        if x[tail-1] == '-':
            return tail
        tail -= 1

def detect_head(x):
    head = 0
    N = len(x)
    while head < N:
        if x[head] == '-':
            return head
        head += 1
    return N

def detect_head_minus(x):
    head = 0
    N = len(x)
    while head < N:
        if x[head] == '-':
            return head
        head += 1
    return N

def move(x):
    head = detect_head(x)
    #print "head", head
    if head > 0:
        for i in range(head):
            x[i] = '-'
        return x
    
    tail = detect_tail(x)
    #print "tail", tail
    
    x_flipped = flip(x[:tail])
    for i in range(tail):
        x[i] = x_flipped[i]
    return x
    
def solve_case(x):
    
    x = list(x)
    moves = 0
    while True:
        if check_solved(x):
            return moves
        x = move(x)
        #print x
        moves += 1      

with open(filename_in) as fin, \
    open(filename_out, 'wb') as fout:
    T = int(fin.readline().strip())
    print T
    for i in range(1, T+1):
        x = fin.readline().strip()
        y = solve_case(x)
        fout.write('Case #%d: %s\n' %(i, str(y)))
