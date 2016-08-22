import sys

#joins consecutive parts together and outputs simplified string
def simplify(str):
    new_str=[]
    curr=None
    for c in str:
        if c != curr:
            curr = c
            new_str.append(c)
    return ''.join(new_str)


def calc_flips(case):
    if len(case) == 1:
            if case=='+':
                return 0
            else:
                return 1
    else:
        if case[0] == '-':
            if case[-1] == '-':
                return len(case)
            return len(case) -1
        else:
            if case[-1] == '-':
                return len(case)
            return len(case)-1
    return 0


def main(argv):
    f = open(argv, 'r')
    N = int(f.readline())

    for i in range(N):
        case = simplify(f.readline().strip())
        print( "Case #%d: %d" % (i+1, calc_flips(case)))



if __name__ == "__main__":
    main(sys.argv[1])