from array import array
data = open('B-large.in','r')
d = open('B-large.out','w')

cases = data.readline()
cases = int(cases)
case_count = 1

while( case_count <= cases):
    pcakes = data.readline()

    pcake = pcakes.strip()
    flips = len(pcake)
    #print(flips)
    counter = 0
    ans = 0

    if(pcake[(flips - 1)] == '-'):
        ans += 1

    while( counter < (flips-1) ):
        counter += 1

        if(pcake[(counter - 1)] != pcake[counter]):
            ans += 1

    print('Case #' + str( case_count) + ': ' + str(ans), file = d)

    case_count += 1

d.close()

