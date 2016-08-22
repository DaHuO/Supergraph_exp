def print_solution(i, solution):
    print "Case #{}: {}".format(i, ''.join(solution))

def handle_case(i):
    s = raw_input()
    output = []
    for c in s:
        if len(output) == 0:
            output.append(c)
        elif c < output[0]:
            output.append(c)
        else:
            output.insert(0, c)
    print_solution(i, output)


def main():
    n = int(raw_input())
    for i in range(n):
        handle_case(i+1)

if __name__ == "__main__":
    main()
