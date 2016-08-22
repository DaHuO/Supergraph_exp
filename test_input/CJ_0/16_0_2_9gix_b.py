"""
  +         0
  -         1
 -+         1 
 +-         1 + c
-+-         
+-+

"""
import itertools
HEAD = '+'
TAIL = '-'

def compute(pancake):
    count = len(''.join(_ for _, __ in itertools.groupby(pancake)))
    return count if pancake[-1] == TAIL else count - 1

def main():
    fname = 'B-large'
    with open(fname+'.in', 'r') as f:
        T, *pancakes = f.readlines()
    pancakes = [compute(_.strip()) for _ in pancakes]
    with open(fname+'.out', 'w') as f:
        for i, pancake in enumerate(pancakes, 1):
            print('Case #{}: {}'.format(i, pancake), file=f)

if __name__ == '__main__':
    main()