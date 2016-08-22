__author__ = 'zfeng'

def solver(line):
    count = 0
    line = line.strip()

    if line[0] == '-':
        status = False
    else:
        status = True

    for i in line[1:]:
        if status:
            if i == '+':
                continue
            else:
                status = False
                count += 1
        else:
            if i == '-':
                continue
            else:
                status = True
                count += 1

    if not status:
        count += 1

    return count

if __name__ == '__main__':
    f = open('/Users/zfeng/Downloads/B-large.in')
    lines = f.readlines()
    f.close()

    for i in xrange(int(lines[0])):
        print str.format('Case #{0}: {1}', i + 1, solver(lines[i + 1]))

