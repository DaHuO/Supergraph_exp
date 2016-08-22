__author__ = 'Christian'

#fname = 'test_a.txt'
fname = 'A-small-attempt0.in'
#fname = 'A-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

def find_last_word(s):
    if s == '':
        return ''
    max_letter = None
    max_letter_index = []
    for i,c in enumerate(s):
        if not max_letter or c > max_letter:
            max_letter_index = []
            max_letter = c
        if c == max_letter:
            max_letter_index.append(i)
    best_word = None
    for max_ind in max_letter_index:
        word = max_letter + find_last_word(s[:max_ind]) + s[max_ind+1:]
        if not best_word or word > best_word:
            best_word = word
        
    return best_word


T = int(data[0])
for i in range(T):
    print >> res_file, "Case #%s: %s" % (i+1, find_last_word(data[i+1]))
    
res_file.close()