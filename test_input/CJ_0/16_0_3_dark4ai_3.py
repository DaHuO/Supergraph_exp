fin = open('C-large.in', 'r')
fout = open('C-large.out', 'w')

def solve(n, j):
    n, j = map(int, fin.readline().split())
    answer = []
    for mask in xrange(2**(n - 2)):
        dvs = []
        number = (1 << (n - 1)) | (mask << 1) | 1
        # print "Check number {}".format(bin(number))
        for base in range(2, 11):
            current = 0
            for i in range(0, n):
                current += min(number & (1 << i), 1) * (base ** i)
            # print "  Base {}, value {}".format(base, current)
            i = 2
            dv = 0
            while i < 5000 and i*i <= current:
                if current % i == 0:
                    dv = i
                    break
                i += 1
            dvs.append(dv)
            if not dv:
                break
        if all(dvs):
            current_answer = '{} {}'.format(bin(number)[2:], ' '.join(map(str, dvs)))
            answer.append(current_answer)
            # print len(answer), current_answer
            j -= 1
            if j == 0:
                break
    return '\n'.join(answer)


# for n in range(2, 17):
#     answer = solve(n, 0)
#     print "N = {}, size = {}".format(n, len(answer.split('\n')))
    # print answer
    # print "#####"



tests_count = int(fin.readline())

for test in range(1, tests_count + 1):
    answer = solve(0, 0)
    fout.write("Case #{}:\n{}\n".format(test, answer))
