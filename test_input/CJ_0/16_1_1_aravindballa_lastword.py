import sys

with open(sys.argv[1], 'r') as f:

    fout = open(sys.argv[2], 'w')

    T = f.readline().strip('\n')

    for i in range(int(T)):
        inp = f.readline().strip('\n')
        result = inp[0]

        for c in inp[1:]:
            if c >= result[0]:
                result = c + result
            else:
                result = result + c

        print result
        fout.write('Case #' + str(i+1) + ': ' + result + '\n')
    fout.close()