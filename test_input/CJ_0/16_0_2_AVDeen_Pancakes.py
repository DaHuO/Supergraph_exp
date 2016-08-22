import sys

__author__ = 'vandeen'

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as fh:
        fh.readline()  # Strip first line, don't need it (Always 1 case)
        output = open("test.out", "w")
        case_num = 1

        for s in fh:
            s = s.rstrip()
            flips = 0
            last = s[0]

            for i in range(1, len(s)):
                if s[i] is not last:
                    flips += 1
                last = s[i]
            if s[-1] is "-":
                flips += 1

            print("Case #%d: %d" % (case_num, flips))  # For debugging
            output.write("Case #%d: %d\n" % (case_num, flips))
            case_num += 1
