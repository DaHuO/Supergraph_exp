
def printCase(val, i, out):
    out.write('Case #' + str(i) + ': ' + str(val) + '\n')
    return


filename = 'B-large.in'
filenameout = 'muhPancakes.out'
f = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem2\\' + filename, 'r')
first = f.readline()
out = open('C:\Users\Brian\Documents\Pythonscratch\GoogleCodeJam2016\Qualifiers\Problem2\\' + filenameout, 'w')

i = 1
count = 0
for line in f:
    count = 0
    prev = '+'
    # for each sequence of -, increment by 2
    for x in line:
        if prev == '+' and x == '-':
            count += 2
            prev = '-'
        if prev == '-' and x == '+':
            prev = '+'
        
    # two cases, starts with - or starts with +
    if line[0] == '-':
        count -= 1
    printCase(count, i, out)
    i += 1
f.close()
out.close()
print 'done'
    
