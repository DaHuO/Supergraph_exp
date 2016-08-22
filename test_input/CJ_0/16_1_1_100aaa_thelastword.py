import sys

def main(argv=sys.argv):
    output = open("output.out", "w")
    input = open("A-small-attempt0 (1).in", "r")
    number_of_tescases = int(input.readline().rstrip())
    for case in range(1, number_of_tescases + 1):
        string = input.readline().rstrip()
        ret = solve(string)
        output.write("Case #" + str(case) + ": " + ret + '\n')
    output.close()
    input.close()

def solve(str):
    str_list = list(str)
    tree = []
    tree.append(str_list[0])
    for i in range(1, len(str_list)):
        length = i
        candidates = []
        for str in tree:
            if len(str) == length:
                candidates.append(str)
            elif len(str) > length:
                break
        for candidate in candidates:
            if candidate[0] > str_list[i]:
                tree.append(str_list[i] + candidate)
                tree.append(candidate + str_list[i])
            else:
                tree.append(candidate + str_list[i])
                tree.append(str_list[i] + candidate)

    return tree[len(tree) - 1]

if __name__ == "__main__":
    main()