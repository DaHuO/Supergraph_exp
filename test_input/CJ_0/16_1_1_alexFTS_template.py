import sys
import math

def func(word):

    word = word.strip()
    curr = ""
    
    while len(word) > 0:
        if curr + word[0] > word[0] + curr:
            curr += word[0]
        else:
            curr = word[0] + curr
        word = word[1:]
    return curr
            
    
def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: python program.py < input')
    
    i = 1
    maximum = int(sys.stdin.readline())
    
    for l in sys.stdin:
        if i > maximum:
            break
            
        print "Case #%i: " %i + func(l)
        i += 1
    return

if __name__ == '__main__':
    main()
