primes = []

def pop_list_primes():
    siv = [0]*((2**16) + 8)
    for i in range(2,len(siv)):
        if siv[i] == 0:
            for j in range(i*2,len(siv),i):
                siv[j]=1
    for i in range(2,len(siv)):
        if siv[i] == 0:
            primes.append(i)

def is_prime(cand):
    for p in primes:
        if p>=cand:
            break
        if cand%p==0:
            return p
    return -1

def read_num(num, base):
    total = 0
    for i, c in enumerate(reversed(num)) :
        if c=='1':
            total += base**i
    return total

def bins(num):
    ret =''
    cur =-1
    while 2**cur <=num:
        cur+=1
    for i in reversed(range(cur)):
        if 2**i <= num:
            ret+='1'
            num -= 2**i
        else:
            ret+='0'
    return ret

def solve(in_file, out_file):
    trials=int(in_file.readline())
    for trial in range(1, trials + 1):
        size, needed = [int(c) for c in in_file.readline().split() ]
        found =[]
        cand =(2**(size-1))+1
        while len(found) < needed:
            num = bins(cand)
            wits=[]
            for i in range(2,11,1):
                wit= is_prime(read_num(num, i))
                if wit!=-1:
                    wits+=[wit]
                else:
                    break
            if len(wits) >= 9:
                found+=[(num, wits)]
            cand+=2
        out_file.write("Case #{}:\n".format(trial))
        for i in range(needed) :
            out_file.write(found[i][0])
            for j in found[i][1]:
                out_file.write(' {}'.format(j))
            out_file.write('\n')

if __name__ == '__main__':
    path=''
    #name='C-sample'
    name='C-small-attempt0'
    #name='B-large'
    raw=open(path+name+'.in', 'r')
    wrt=open(path+name+'.out','w')
    pop_list_primes()
    #print(primes)
    solve(raw, wrt)
    raw.close()
    wrt.close()