import sys
import time
start_time = time.time()
sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")

# import random
# for i in range(100):
#     print(random.randint(10**5,10**6))

def last_minus(arr):
    ans = -1
    for i in range(len(arr)):
        if arr[i] == '-':
            ans = i
    return ans

def flip(arr, index):
    for i in range(index + 1):
        if arr[i] == '-':
            arr[i] = '+'
        else:
            arr[i] = '-'
    return arr


sys.stdout = open("output.txt", "w")
sys.stdout = sys.__stdout__
for testcases in range(int(input())):
    pancakes = input()
    arr = []
    for i in pancakes:
        arr.append(i)
    ans = 0
    while True:
        res = last_minus(arr)
        if res == -1:
            break
        ans += 1
        arr = flip(arr, res)

    sys.stdout = open("output.txt", "a")
    print("Case #" + str(testcases + 1) + ": " + str(ans) )
    sys.stdout = sys.__stdout__
    print("Case #" + str(testcases + 1) + ": Done")

sys.stdout = sys.__stdout__
print(time.time() - start_time)