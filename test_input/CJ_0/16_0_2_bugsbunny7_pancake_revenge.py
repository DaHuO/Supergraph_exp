
def do_flip(pancakes,flip_to):
    i = 0
    while i < flip_to+1:
        if pancakes[i] == '-':
            pancakes[i] = '+'
        else:
            pancakes[i] = '-'
        i += 1

filename = 'B-large.in.txt'
with open(filename,'r') as finput, open('A-pancake.out.txt','w') as output:
    lines = [line for line in finput]
    test_cases = int(lines[0])

    for j in range(1, test_cases+1):
        pancakes = list(lines[j].strip())
        flip = 0
        
        #check each pancake for +
        i = 0
        while i < len(pancakes):
            if pancakes[i] == "-":
                if i == len(pancakes)-1 or pancakes[i+1] == "+":
                    do_flip(pancakes,i)
                    flip += 1
                    i = -1 # iterate from beginning again
            i += 1

        output.write( "Case #%d: %d\n" % (j, flip) )
