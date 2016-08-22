problem_name = 'last_word'
#ifilename = 'test.in'
#ifilename = 'A-small-attempt0.in'
ifilename = 'A-large.in'
ofilename = 'solution--' + problem_name + '--' + ifilename.split('.')[0] + '.txt'

ifile = open(ifilename, 'r')
num_cases = int(ifile.readline())

ofile = open(ofilename, 'w')

class Case:
    pass
    
def next_case(f):
    line = f.readline()
    if line == '':
        return []

    c = Case()
    c.s = line.strip()
    return c

def find_ans_str(c):
    ans_str = ''

    before = []
    after = []
    l = [x for x in c.s]
    first = l[0]
    after.append(first)
    for c in l[1:]:
        if c >= first:
            before.append(c)
            first = c
        else:
            after.append(c)

    ans_str = ''.join(reversed(before)) + ''.join(after)
    return ans_str

c = next_case(ifile)
casenum = 1
while c != []:

    ans_str = 'Case #' + str(casenum) + ': '
    ans_str += find_ans_str(c)
#    print(ans_str)
    ofile.write(ans_str + '\n')
    c = next_case(ifile)
    casenum += 1

if casenum - 1 != num_cases:
    print('error: not all cases read')
ifile.close()
ofile.close()
