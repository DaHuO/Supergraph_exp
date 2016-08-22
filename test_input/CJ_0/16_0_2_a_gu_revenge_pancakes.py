def flip(pancakes):
    return [not pancake for pancake in pancakes[::-1]]


def shuffle(stack, index):
    return flip(stack[:index + 1]) + stack[index + 1:]

f = open("B-large.in", "r")
f2 = open("out.txt", "w")
n = int(f.readline())
for i in range(n):
    pancakes = [i == "+" for i in f.readline().strip("\n")]
    count = 0
    while not all(pancakes):
        index = 0
        start = pancakes[index]
        while index < len(pancakes) and pancakes[index] == start:
            index += 1
        pancakes = shuffle(pancakes, index - 1)
        count += 1
    output = "Case #" + str(i + 1) + ": " + str(count)
    f2.write(output + "\n" if i != n - 1 else output)
f.close()
f2.close()