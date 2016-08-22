import sys
def read(): return sys.stdin.readline().rstrip()
def read_int(): return int(read())

T = read_int()

def winning_word(string):
    result = [string[0]]
    for i in range(1, len(string)):
        current_letter = string[i]
        if result[0] > current_letter:
            result.append(current_letter)
        else:
            result.insert(0, current_letter)
    return "".join(result)

for t in range(T):
    given = read()
    print("Case #{}: {}".format(t+1, winning_word(given)))