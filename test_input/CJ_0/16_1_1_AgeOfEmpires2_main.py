import sys
import time
start_time = time.time()
sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")


sys.stdout = open("output.txt", "w")
sys.stdout = sys.__stdout__
for testcases in range(int(input())):

    word = input()
    if len(word) == 1:
        sys.stdout = open("output.txt", "a")
        print("Case #" + str(testcases + 1) + ": " + word)
        sys.stdout = sys.__stdout__
        print("Case #" + str(testcases + 1) + ": Done")
        continue
    res = []
    res.append(word[0])
    if word[1] >= res[0]:
        res.insert(0, word[1])
    else:
        res.append(word[1])
    for i in range(2, len(word)):
        if word[i] >= res[0]:
            res.insert(0, word[i])
        else:
            res.append(word[i])

    sys.stdout = open("output.txt", "a")
    print("Case #" + str(testcases + 1) + ": " + ''.join(res))
    sys.stdout = sys.__stdout__
    print("Case #" + str(testcases + 1) + ": Done")

sys.stdout = sys.__stdout__
print(time.time() - start_time)