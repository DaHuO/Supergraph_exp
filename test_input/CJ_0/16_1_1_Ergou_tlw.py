from collections import deque
def last_word(S):
    res = deque(S[0])
    for ch in S[1:]:
        if ord(ch) >= ord(res[0]):
            res.appendleft(ch)
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == '__main__':
    with open('A-large.in') as fin, open('A-large.out', 'w') as fout:
        fin.readline()
        for i, line in enumerate(fin, 1):
            fout.write('Case #%d: %s' % (i, last_word(line)))