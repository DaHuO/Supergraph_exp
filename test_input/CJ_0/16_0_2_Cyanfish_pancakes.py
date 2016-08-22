import jam

def count(array, goal):
    if len(array) == 0:
        return 0
    if array[-1] == goal:
        return count(array[0:-1], goal)
    else:
        return count(array[0:-1], 1 - goal) + 1

def solve(case):
    s = case.readLine()
    array = []
    for char in s:
        if char == "+":
            array.append(1)
        elif char == "-":
            array.append(0)
    return count(array, 1)

jam.run("B-large.in", solve)
