import sys

with open(sys.argv[1], 'r') as f:

    fout = open(sys.argv[2], 'w')

    T = f.readline().strip('\n')

    for i in range(int(T)):

        input = f.readline().strip('\n')
        flips = 0

        while '-' in input:

            if '+' not in input:
                flips += 1
                break

            flip_at = input.find('+')
            if flip_at == 0:
                flip_at = input.find('-')
            flipping = input[:flip_at]


            flipping = list(flipping)
            flipping.reverse()

            flipped = []
            for c in flipping:
                if c == '-':
                    flipped.append('+')
                else:
                    flipped.append('-')

            input = ''.join(flipped) + input[flip_at:]

            flips += 1

        print flips
        fout.write('Case #' + str(i + 1) + ': ' + str(flips) + '\n')

    fout.close()