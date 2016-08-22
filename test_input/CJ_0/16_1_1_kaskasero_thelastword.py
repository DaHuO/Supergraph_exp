# Code Jam 2016
# Round 1
# Raoul Veroy
import fileinput

stdin = fileinput.input()

def get_last_word( word ):
    ans = [ word[0] ]
    for x in word[1:]:
        if x >= ans[0]:
            ans.insert( 0, x )
        else:
            ans.append( x )
    return "".join( ans )

count = int(stdin.next())
for x in xrange(count):
    word = stdin.next().rstrip()
    ans = get_last_word( word )
    print "Case #%d: %s" % (x+1, ans)
