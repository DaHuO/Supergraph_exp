def read_word(f):
    return next(f).strip()

def read_int(f, b=10):
    return int(read_word(f), b)

def read_letters(f):
    return list(read_word(f))

def read_digits(f, b=10):
    return [int(x, b) for x in read_letters(f)]

def read_words(f, d=' '):
    return read_word(f).split(d)

def read_ints(f, b=10, d=' '):
    return [int(x, b) for x in read_words(f, d)]

def read_floats(f, d=' '):
    return [float(x) for x in read_words(f, d)]

def read_arr(f, R, reader=read_ints, *args, **kwargs):
    return [reader(f, *args, **kwargs) for i in range(R)]

#..............................................................................


def read_case(f):
    Q1 = read_arr(f, 4)
    return (Q1)
    

def write_case(f, i, res):
    f.write('Case #%d: '%i)
    f.write('%s'%res)
    f.write('\n')


#..............................................................................

def begin(fn='a', out_fn=None):
    in_fn = fn + '.in'
    if out_fn is None:
        out_fn = fn + '.out'
    with open(in_fn, 'r') as fi:
        with open(out_fn, 'w') as fo:
            T = read_int(fi)
            for i in range(1,T+1):
                case = read_word(fi)
                res = solver(case)
                write_case(fo, i, res)



#..............................................................................



def flip(k,L,ctr):
   l=k-1
   while l>=0:
      if L[l]=='+':
         L[l]='-'
      elif L[l]=='-':
         L[l]='+'
      l-=1
      k=-1
   ctr+=1
   k=0
   return k,L,ctr
def solver(st):
   inp=st
   while inp.count('--')!=0 or inp.count('++')!=0:
      inp=inp.replace('--','-')
      inp=inp.replace('++','+')
   L=[]
   for j in inp:
      L.append(j)
   k=0
   ctr=0
   for k in range(len(L)):
      if L[0]=="-" and L[k]=='-':
         ctr=k+1
         L[k]=="+"
      elif L[0]=="+" and L[k]=='-':
         ctr=k+1
   return ctr
begin('2_large')
