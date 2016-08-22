fin = "input.txt"
fout = "output.txt"

tests = []
for line in open(fin, "r"):
    tests.append(line.strip())

j = 0
with open(fout, "w") as f:
    for test in tests[1:]:
        j += 1
        for i in range(len(test)):
            test = test.replace("--", "-")
            test = test.replace("++", "+")
        #print("{} {}\n".format(test, int(test[-1] == "-")))
        answer = len(test) - 1 + int(test[-1] == "-")
        f.write("Case #{}: {}\n".format(j, answer))