import sys

def bitcoin(line):
    ret = {}
    arr = line.split(" ")
    length, amount = int(arr[0]), int(arr[1])
    init_number = 1<<(length-1)
    j = 1
    succeed_amount = 0
    while succeed_amount != amount:
        target = bin(init_number + j)[2:]
        if len(target) > length:
            break
        succeed_number_base = {}
        for divisor in xrange(2, 100):
            check_divisor(target, divisor, succeed_number_base)
            if len(succeed_number_base) == 9:
                ret[target] = succeed_number_base
                succeed_amount += 1
                break
        j += 2
    return ret

def check_divisor(number, divisor, succeed_number_base):
    info = [[1]+ [0] * (len(number)-1) for _ in range(11)]
    for number_base in range(2, 11):
        if number_base in succeed_number_base:
            continue
        for i in range(1, len(info[0])):
            info[number_base][i] = info[number_base][i-1] * number_base % divisor
    for number_base in range(2, 11):
        if number_base in succeed_number_base:
            continue
        sum_v = 0
        for i, ch in enumerate(reversed(number)):
            sum_v += int(ch) * info[number_base][i]
        if sum_v % divisor == 0:
            succeed_number_base[number_base] = divisor

if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    file.readline()
    i = 0
    for line in file:
        i += 1
        if line.strip() == "":
            continue
        r = bitcoin(line)
        print "Case #%d:" % i
        for k, v in sorted(r.items()):
            print k,
            v = sorted(v.items())
            for _, divisor in v:
                print divisor,
            print ""
