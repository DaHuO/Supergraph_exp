def main():
    cases = int(input())
    for t in range(cases):
        pattern = [c for c in input()]
        flips = 0
        while '-' in pattern:
            flip(pattern)
            flips += 1
        print("Case #"+str(t+1)+": "+str(flips))


def flip(pattern):
    # find the end of the first sequence and invert it
    char = pattern[0]
    end = 0
    while end < len(pattern) and pattern[end] == char:
        pattern[end] = '+' if char == '-' else '-'
        end += 1


main()