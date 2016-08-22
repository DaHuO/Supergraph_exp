def reverse(s):
    m = ""
    for i in s[::-1]:
        if i == "+":
            m += "-"
        else:
            m += "+"
    return m
def flip(stack, i):
    return reverse(stack[:i + 1]) + stack[i + 1:]


def solve(stack):
    count = 0
    while "-" in stack:
        rindex = stack.rfind('-')

        lindex = stack.find('-')
        if lindex != 0:
            stack = flip(stack, lindex - 1)
            count += 1

        stack = flip(stack, rindex)
        count += 1
    return count


def main():
    f = open("input.txt", 'r')
    lines = f.readlines()
    f.close()

    outFile = open("out.txt", 'w')
    for i, n in enumerate(lines[1:]):
        out = "Case #"+str(i + 1)+": " + str(solve(n))+"\n"
        outFile.write(str(out))


main()