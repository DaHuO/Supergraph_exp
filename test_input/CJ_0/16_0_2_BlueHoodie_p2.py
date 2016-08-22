file = open("C:\Users\Luca\Downloads\B-large.in", "r")
file2 = open("ans.txt", "w")

times = file.readline()

def flipzero(string, max, num):
    new_str = ""
    for char in range(0, max):
        if string[char] == "-":
            new_str = new_str + "+"
        else:
            new_str = new_str + "-"

    new_str = new_str + string[max:]

    num += 1
    return new_str, num

for time in range(int(times)):

    x = file.readline().rstrip()

    a = 0
    perfect = "+" * len(x)

    while x != perfect:

        if x == "-" * len(x):
            a += 1
            break

        if x[0] == "+":
            i = x.find("-")
            x, a = flipzero(x, i, a)
        else:
            i = x.find("+")
            x, a = flipzero(x, i, a)

    s = "Case #" + str(time + 1) + ": " + str(a) + "\n"
    file2.write(s)