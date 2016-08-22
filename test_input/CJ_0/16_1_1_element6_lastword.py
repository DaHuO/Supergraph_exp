import sys
# t=int(raw_input())
# n,j=map(int,raw_input().split())

with open(sys.argv[1], 'r') as f:
    with open(sys.argv[1]+'.out', 'w') as fo:
        f = open(sys.argv[1])
        T = int(f.readline())

        for t in xrange(1, T+1):
            word = f.readline()[:-1]

            left = 0
            right = len(word)

            while left < right:
                right = word.rindex(max(word[left:right+1]), left, right+1)
                if right == left: break

                # print 'stat', word, right, max(word[left:right+1]), left
                # print 'left', word[:left]
                # print 'right', [word[right]]
                # print 'mid', word[left:right]
                # print 'stable', word[right+1:]


                word = word[:left] + word[right] + word[left:right] + word[right+1:]

                # print 'current', word


                left += 1

            # print word
            s = "Case #" + str(t) + ": " + word
            print s

        # n,j = map(int, .split())
        # res,divs=get(n,j)
        # fo.write('Case #1:\n')
        # print "Case #1:"
        #
        # for i in res:
        #     s = i + " ".join(divs) + '\n'
        #     print s,
        #     fo.writelines(s)

