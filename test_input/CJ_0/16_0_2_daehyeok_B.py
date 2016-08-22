import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def rStrip(line):
    for i in range(len(line)-1,-1,-1):
        if line[i] == False:
            return line[:i+1]
        
    return line

def flip(line):
    line.reverse()
    line = [not i for i in line]
    return line

def lflip(line):
    length = 0
    for length in range(len(line)):
        if line[length] == False:
            break
    #length+=1
    line[:length] = flip(line[:length])
    return line
    
        
def check(line):
    for t in line:
        if t == False:
            return False
    return True

def solve(line):
    count = 0
    line = list(map(lambda x : True if x == '+' else False , line))
    
    while check(line) == False:
        line = rStrip(line)        
        if line[0] == True and line[len(line)-1] == False:
            line= lflip(line)            
            count +=1
            
        line = rStrip(line)        
        line = flip(line)
        count +=1
        if check(line):
            break;
        
        
        
    return count

def main():
    t = int(input())

    for i in range(t):
        line = input()
        print("Case #%d: %d" % ((i + 1), solve(line)) )
#        print(line,  solve(line) )
        
        
def log(*message):
    logging.debug(*message)
    #print(*message)
    
if __name__ == "__main__":
    main()
