def main():
    T = int(raw_input())
    for i in range(T):
        line = raw_input()
        prev = line[0]
        count = 0
        for c in line[1:]:
            if c != prev:
                count += 1
            prev = c
        if line[-1] == '-':
            count += 1
        print "Case #{0}: {1}".format(i+1, count)
if __name__ == "__main__":
    main()
