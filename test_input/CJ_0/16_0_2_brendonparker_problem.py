from sys import argv

input_file = argv[1]+'/B-large.in'
f = open(input_file)
o = open(input_file.replace('.in', '.out'), 'w')

test_count = int(f.readline())

def endsWith(l, val):
    length = len(l)
    if length > 0:
        return l[length-1] == val
    else:
        return False

for case_number in range(1, test_count+1):

    print 'Case %d' % case_number
    
    temp = list(str.rstrip(f.readline()))
    
    last = None
    pancakes = []
    for pancake in temp:
        if last == None:
            pancakes.append(pancake)
        else:
            if pancake != last:
                pancakes.append(pancake)
        last = pancake
    
    answer = 0
    
    if pancakes[len(pancakes)-1] ==  '+':
        pancakes.pop()
    
    if len(pancakes) == 1:
        if pancakes[0] == '-':
            answer = 1
    elif len(pancakes) > 1:
        answer += len(pancakes)
    print pancakes        
    o.write("Case #%d: %d\n" % (case_number, answer))

print 'Done'