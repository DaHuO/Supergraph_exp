def read_case(f):
    return next(f)

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')

def begin(fn='a', out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = int(next((fi)))
            for i in range(1,T+1):
                case = read_case(fi)
                res = solver(case)
                write_case(fo, i, res)

#.............................................................................

def flip(string):
    string= string[::-1]
    _string=''
    for ch in string:
        if ch=='+':
            _string+='-'
        else:
            _string+='+'
    return _string



def solver(ln):
    line=ln.split()[0]
    n=0
    for i in range(1,len(line)):
        if line[i] != line[i-1]:
            line= flip(line[:i]) + line[i:]
            n+=1
    if(line[-1]=='-'):
        n+=1
    return n


begin('e')
