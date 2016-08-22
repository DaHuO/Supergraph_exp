def pancakeFlip(s):
    length = len(s)
    stack = []
    for i in range(length):
        if s[i] == '+':
            stack.append(True)
        else:
            stack.append(False)
    flip = 0
    state = True
    for i in range(length):
        if state != stack.pop():
            state = not state
            flip += 1
    return flip

def main():
    t = int(input())
    for i in range(1, t+1):
        case = str(input())
        print("Case #{}: {}".format(i, pancakeFlip(case)))

if __name__ == "__main__":
    main()