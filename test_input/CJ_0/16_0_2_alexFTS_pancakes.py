import sys

def flip(string, sign):
    def change_sign(sgn):
        if sgn == '+':
            return '-'
        else:
            return '+'
            
    def flip_helper(s):
        diff_sign = map(change_sign, s[::-1])
        return ''.join(diff_sign)
        
    result = 0
    if string == "":
        return result
        
    n = len(string)
    i = n - 1
    
    if string[i] == sign:
        return flip(string[:i], sign)
    else:
        # count '-'
        if string[0] == sign:
            result += 1 # flipped
            return result + flip(flip_helper(string), change_sign(sign))
        else:
            return result + 1 + flip(string[:i], change_sign(sign))
            
            
    
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python program.py < input')
    
    i = 1
    maximum = int(sys.stdin.readline())
    
    for l in sys.stdin:
        if i > maximum:
            break
            
        print "Case #%i: %d" % (i, flip(l.strip('\n'), '+'))
        i += 1
    return

if __name__ == '__main__':
    main()
