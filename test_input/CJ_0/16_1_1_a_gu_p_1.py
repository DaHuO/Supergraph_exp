in_file = open("A-large.in", "r")
out_file = open("out.txt", "w")
n = int(in_file.readline().strip("\n"))
for i in range(n):
    s = in_file.readline().strip("\n")
    result = s[0]
    for char in s[1:]:
        if char >= result[0]:
            result = char + result
        else:
            result += char
    out_file.writelines("Case #" + str(i + 1) + ": " + result + ("\n" if i != n - 1 else ""))
