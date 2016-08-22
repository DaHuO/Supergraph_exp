def solve(S):
    new_str = []
    for letter in S:
        if len(new_str) == 0 or letter >= new_str[0]:
            new_str.insert(0, letter)

        else:
            new_str.append(letter)

    final = "".join(new_str)
    return final

if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        S = str(input())
        print("Case #%i: %s" % (case_num, solve(S)))
