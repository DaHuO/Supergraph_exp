import math

tbl = [[j**i for i in range(32)] for j in range(11)]

def getnum(k, num):
    pos = 0
    curr = num
    ret = 0
    while curr>0:
        if curr&1 == 1:
            ret += tbl[k][pos]
        pos += 1
        curr = curr >> 1
    return ret

def getdiv(num):
    curr = 2
    sq = int(math.sqrt(num)+1)
    found = False
    ret = -1
    while curr<sq:
        #print("curr: "+str(curr))
        if curr>10000:
            break;
        if num%curr==0:
            found = True
            ret = curr
            break
        curr = curr + 1
    return ret

def solve():
    n = 32
    j = 500
    found = 0
    i = 1<<(n-1)
    while found<j:
        if (i&1)!=1 or ((i>>(n-1))&1)!=1:
            i = i+1
            continue;
        arr = [0 for i in range(9)]
        good = True;
        for k in range(2,11):
            num = getnum(k, i);
            div = getdiv(num);
            if div==-1:
                good = False;
                break;
            arr[k-2] = div;
        if good:
            print(format(i, 'b')+' '+' '.join([str(x) for x in arr]))
            found = found +1
        i = i+1

if __name__ == "__main__":
    print("Case #1:")
    solve()