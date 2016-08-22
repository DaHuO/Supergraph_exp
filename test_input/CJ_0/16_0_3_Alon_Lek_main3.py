def appendToFile(filename, text):
    with open(filename,'a') as f:
        f.write(text + '\n')

def foundDivider(num):
    for i in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]:
        if num % i == 0:
            return i
    return -1

foundNum = 0
startInBase10 = long("10000000000000000000000000000001", 2)
endInBase10 = long("11111111111111111111111111111111", 2)
appendToFile('output2.txt', "Case #1:")
num = startInBase10 - 1
while True:
    num += 1
    binString = bin(num)[2:]
    if binString[31] != '1':
       continue

    nums = []
    nums.append(int(binString, 2))
    nums.append(int(binString, 3))
    nums.append(int(binString, 4))
    nums.append(int(binString, 5))
    nums.append(int(binString, 6))
    nums.append(int(binString, 7))
    nums.append(int(binString, 8))
    nums.append(int(binString, 9))
    nums.append(int(binString, 10))

    dividers = ""
    flag = 0
    for j in xrange(0,len(nums)):
        divider = foundDivider(nums[j])
        if divider == -1:
            flag = 1
            break

        dividers += str(divider) + " "

    if flag == 0:
        appendToFile('output2.txt', binString + " " + dividers)
        foundNum += 1

    if foundNum == 500:
        break


