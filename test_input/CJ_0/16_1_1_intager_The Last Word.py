import os, time, sys

case_start, case_end = 1, 100

cur_dir=os.path.dirname( os.path.abspath(__file__) )
output=None

def log( msg ):
    print msg
    output.write( msg + '\n' )

lines=[]
for f in os.listdir( cur_dir ):
    if f.lower().endswith( '.in' ):
        if not 'output' in f:
            lines=open( os.path.join( cur_dir, f ), 'r' ).readlines()
            outpath=f.split( '.' )[0] + '_output_%d_%d.txt' % (case_start, case_end)
            print f, '-->', outpath
            output=open( os.path.join( cur_dir, outpath ), 'w' )
            break

start = time.time()

# ------------------------------------------------------- 

best=''
s="CABCBBABC"

def rec( index, word ):
    global best

    if index==len(s):
        if word > best:
            best=word
            print word
        return

    rec( index+1, word+s[index] )
    rec( index+1, s[index]+word)

def greed():
    ans=s[0]

    i=1
    while i<len(s):
        c=s[i]
        left=c+ans
        right=ans+c
        if right>left:
            ans=right
        else:
            ans=left
        i+=1

    '''
    for i,c in enumerate(s):
        if not s[i+1:]: break
        if c>=max( s[i+1:] ):
            ans=c+ans
        else:
            ans+=c
    '''

    return ans

n=-1

def solve():
    global best
    best=''
    rec(0,'')
    return best

#solve()
#print best
#sys.exit(0)

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    s=lines[k].strip(); k+=1

    if case>=case_start and case<=case_end:
        #ans=solve()
        g=greed()
        log( 'Case #%d: %s' % (case,g) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
