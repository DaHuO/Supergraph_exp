alpha = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, \
          'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, \
          'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, \
          'Z':26 }
def winner(S):
    newstr = S[0]
    for i in range(1,len(S)):
        if alpha.get(S[i]) >= alpha.get(newstr[0]):
            newstr = S[i] + newstr
        else:
            newstr += S[i]
    return newstr

if __name__ == '__main__':
    T = int(raw_input())
    for zz in range(0,T):
        S = raw_input()
        print "Case #%s: %s" % (str(zz+1),winner(S))
