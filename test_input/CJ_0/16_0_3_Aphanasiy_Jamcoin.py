def get(w):
    i = 2
    c = 0
    while (i * i <= w):
        if w % i == 0:
            c = w // i
        i += 1
    return c


cnt = 0
def check(s, fout):
    global cnt
    u = []
    for i in range(2, 11):
        g = get(int(s, i))
        if g: u.append(g)
        else: return False
    fout.write(s + ''.join([" {}" for i in range(9)]).format(*u) + '\n')
    return True


n, k = map(int, input().split())
s = (1 << (n - 1)) + 1
fout = open("Jamcoin.out", 'w')
fout.write("Case #1:\n")
while (len(bin(s)) == n + 2 and k > cnt):
    if check(bin(s)[2:], fout):
        cnt += 1
        print("{}/{}".format(cnt, k), flush=True)
    s += 2
fout.close()
