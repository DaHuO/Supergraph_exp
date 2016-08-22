import itertools, math

def get_factor(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return 0

t = int(raw_input())
for i in xrange(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]
    p = list(itertools.product([0, 1], repeat=n-2))
    print "Case #{}:".format(i)
    j = j - 1
    for k in p:
        base_two = 2**(n-1) + 1
        base_three = 3**(n-1) + 1
        base_four = 4**(n-1) + 1
        base_five = 5**(n-1) + 1
        base_six = 6**(n-1) + 1
        base_seven = 7**(n-1) + 1
        base_eight = 8**(n-1) + 1
        base_nine = 9**(n-1) + 1
        base_ten = 10**(n-1) + 1
        for a,b in enumerate(k):
            if b == 1:
                base_two = base_two + 2**(n-2-a)
                base_three = base_three + 3**(n-2-a)
                base_four = base_four + 4**(n-2-a)
                base_five = base_five + 5**(n-2-a)
                base_six = base_six + 6**(n-2-a)
                base_seven = base_seven + 7**(n-2-a)
                base_eight = base_eight + 8**(n-2-a)
                base_nine = base_nine + 9**(n-2-a)
                base_ten = base_ten + 10**(n-2-a)
        if get_factor(base_two) and get_factor(base_three) and get_factor(base_four) and get_factor(base_five) and get_factor(base_six) and get_factor(base_seven) and get_factor(base_eight) and get_factor(base_nine) and get_factor(base_ten):
            print"1{}1 {} {} {} {} {} {} {} {} {}".format(''.join(map(str, k)), get_factor(base_two), get_factor(base_three) , get_factor(base_four) , get_factor(base_five) , get_factor(base_six) , get_factor(base_seven) , get_factor(base_eight) , get_factor(base_nine) , get_factor(base_ten))
            if j:
                j = j - 1
            else:
                break