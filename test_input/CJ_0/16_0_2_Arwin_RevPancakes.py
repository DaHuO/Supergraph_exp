__author__ = 'Arwin'
fn= 'B-large.in'
f = open( fn )
ansf = open("ans.txt", "w")

def pancake(str):
    l= filter(None, str.split('+'))
    n= len(l)
    if n==0:
        return 0
    if str[0]=='+':
        return 2*n
    else:
        return 2*n-1

T= int(f.next())
for i in xrange(1,T+1):
    seq= f.next().strip()
    ansf.write( 'Case #{0}: {1}\n'.format(i, pancake(seq)) )

ansf.close()
