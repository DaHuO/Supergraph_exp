def main():
    t = int(input())
    for i in range(1, t + 1):
        pancakes(i, raw_input())

def pancakes(index, stack):
    transitions = 0
    stack = stack + '+'
    last = stack[0]
    for i in range(1, len(stack)):
        current = stack[i]
        if last != current:
            transitions += 1
            last = i
        last = current
    print('Case #{index}: {answer}'.format(index=index, answer=transitions))

if __name__ == "__main__":
    main()
