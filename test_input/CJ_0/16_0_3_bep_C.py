
def gen_num(mid_id, length):
    f = "1{:0" + str(length/2 - 2) + "b}1"
    return f.format(mid_id) * 2

def gen_factors(length):
    return [i**(length/2) + 1 for i in range(2, 11)]

def check(num, factors):
    ret = []
    for i in range(2, 11):
        x = int(num, i)
        if not (x % int(factors[i-2]) == 0):
            print "ERROR",num,i, x, int(factors[i - 2])
            assert False


length = 32
J = 500

print "Case #1:"
for i in range(1, J+1):
    num = gen_num(i, length)
    factors = gen_factors(length)
    print num + " " + " ".join(map(str,factors))
    check(num, factors)
