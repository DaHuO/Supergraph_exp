from itertools import count
f = open('C-large.in', 'r')
output = open('output.txt', 'w')


def jam_list(N,J):
    deci_list = []
    for k in count(2**(N-1)+1,6):
        if len(deci_list) == J:
            break
        temp = bin(k)[2:]
        status = True
        for m in range(3, 11):
            if int(temp, m) % (m+1) != 0:
                status = False
                break
        if status:
            deci_list.append(temp)
    return deci_list
T = int(f.readline().strip())
for k in range(T):
    N, J = [int(x) for x in f.readline().strip().split(' ')]
    res = jam_list(N,J)
    output.write('Case #{0}:\n'.format(k+1))
    for i in range(J):
        output.write('{0} 3 4 5 6 7 8 9 10 11\n'.format(res[i]))
f.close()
output.close()

