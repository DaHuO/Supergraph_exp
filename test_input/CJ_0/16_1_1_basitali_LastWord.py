def last_word(input):
    word = input[0]
    for i in input[1:]:
        if i >= word[0]:
            word = i + word
        else:
            word = word + i
    
    return word

if __name__ == '__main__':
    case = 'A-large'
    inp = open('%s.in'%case);
    out = open('%s.out'%case, 'w');

    cases = int(inp.readline())
    for i in xrange(1, cases + 1):
        input = inp.readline()
        o = "Case #%d: %s"%(i, last_word(input))
        print o
        out.write('%s'%o)
        if i < cases:
            out.write('\n')
