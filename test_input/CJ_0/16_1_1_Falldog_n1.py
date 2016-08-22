import sys

def last_word(word):
    res = ''
    for w in word:
        if len(res) == 0:
            res = w
        elif w >= res[0]:
            res = w + res
        else:
            res = res + w
    return res
        
        

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        count = int(f.readline())
        for i in range(count):
            line = f.readline()
            word = last_word(line.strip())
            print 'Case #%d: %s' % (i+1, word)
    

if __name__ == '__main__':
    main()
