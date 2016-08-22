import sys
import cProfile
import time

from pc_stack import PC_stack
import queue as Q

def solve_file(filen):
    f = open(filen + '.in', 'r')
    T = int(f.readline())
    print(T)

    ans = ""

    for i in range(1, T+1):
        st = f.readline().strip()
        nans = solve_st_alt(st)
        ans += "Case #%d: %s\n" % (i, nans)
        print('#%d done!' % i)

    f = open(filen + '.out', 'w')
    f.write(ans)
    print('Done!')

def solve_st_alt(st_s):
    st = [c_to_int(c) for c in st_s]
    n = 0
    L = len(st)
    while sum(st) > 0:
        n += 1
        f = st[0]
        ind = 0
        while ind < L and st[ind] == f:
            ind += 1
        st[:ind] = [1-x for x in st[:ind]]
    return n

def c_to_int(c):
    if c == '+':
        return 0
    elif c == '-':
        return 1

def solve_st(st_s):
    q = Q.PriorityQueue()
    st = PC_stack(st_s)
    if st.is_done():
        return 0

    q.put(st)
    while True:
        st = q.get()
        for s in st.flips():
            if s.is_done():
                return s.moves
            q.put(s)

"""def flips(ll):
    fl = []
    l = range(1, len(ll) + 1)
    f = partial(flip, ll = ll)
    with Pool(1) as p:
        fl = p.map(f, l)

    return fl

def flip(ll, n):
    ret = ll.copy()
    temp = reversed(ll[:n])
    temp = [1-x for x in temp]
    ret[:n] = temp
    return ret

def is_finished(l):
    for ll in l:
        if sum(ll) == 0:
            return True
    return False"""

if __name__ == '__main__':
    for filen in sys.argv[1:]:
        pr = cProfile.Profile()
        pr.enable()
        #start_time = time.time()
        solve_file(filen)
        #print("--- %s seconds ---" % (time.time() - start_time))
        pr.disable()
        pr.print_stats(sort="tottime")