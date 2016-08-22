"""
def numberOfTimes(case):
    seen_letters = []
    for i in list(str(case)):
        if i not in seen_letters:
            seen_letters.append(i)
    n = 1
    number = n * case
    while len(seen_letters) < 10:
        number = n*case
        n+=1
        for i in list(str(number)):
            if i not in seen_letters:
                seen_letters.append(i)
        if n > 1000:
            return "INSOMNIA"
    return number
"""

def trimRight(order):
    if order == "+":
        return ""
    if order[len(order) - 1] == "+":
        return trimRight(order[:-1])
    else:
        return order 

def flip(order):
    flippedOrder = ""
    for i in order:
        if i == "+":
            flippedOrder = flippedOrder + "-"
        if i == "-":
            flippedOrder += "+"
    return flippedOrder

def pancakeFlips(order):
    flips = 0
    while len(order) > 0:
        order = trimRight(order)
        order = flip(order)
        flips += 1
    return flips - 1 

dataFile = open("B-large.in")
data = []
for i in dataFile:
    data.append(i)
index = 0
for i in data:
    if index < len(data) - 1:
        data[index] = data[index][:-1]
    index+=1


print data

answer = open("googleCodeJamDumpFile.in", 'w')
cases = data[0]
for i in range(1,len(data)): 
    answer.write("Case #" + str(i) + ": " + str(pancakeFlips(data[i])))
    if i < len(data) - 1:
        answer.write("\n")
