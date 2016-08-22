# Count
t = int(input())


def iter_input():
    for i in range(1, t + 1):
        yield (i, input())

#
def solve(sequence, string):
    last = "+"
    answer = 0
    for char in reversed(string):
        if char!= last:
            last = char
            answer += 1

    print("Case #{0}: {1}".format(sequence, answer))



if __name__ == "__main__":
    # python count-sheep.py < input.txt
    for seq, string in iter_input():
        solve(seq, string)
