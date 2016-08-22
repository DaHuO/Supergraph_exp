def main():
    T = int(input())
    for case_num in range(1, T + 1):
        s = input()
        o = [s[0]]
        for c in s[1:]:
            if c >= o[0]:
                o.insert(0, c)
            else:
                o.append(c)
        print("Case #{0}: {1}".format(case_num, ''.join(o)))

main()
