def main():        
    t = int(raw_input())  
    for tn in xrange(1, t + 1):
        n = raw_input()
        lst = []
        for l in n:
            if l == "-":
                lst.append(0)
            elif l == "+":
                lst.append(1)

        ctr = 0
        while 1:
            ind = 0
            f = 0
            while ind < len(lst) and lst[ind] == 1:
                f = 1
                ind += 1

            if ind == len(lst):
                break
            if f == 1:
                for i in range(ind):
                    lst[i] = 0
                ctr += 1
                continue

            ind = 0
            while ind < len(lst) and lst[ind] == 0:
                ind += 1

            for i in range(ind):
                lst[i] = 1
            ctr += 1

        print "Case #{}:".format(tn),

        print "{}".format(ctr)


if __name__ == '__main__':
    main()
