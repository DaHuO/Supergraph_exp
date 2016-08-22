def revenge_of_pancakes(s):

    result = 0
    prev_char = "+"
    curr_char = ""

    for i in range(len(s)-1, -1, -1):
        curr_char = s[i]
        if curr_char == prev_char:
            continue

        result += 1
        prev_char = curr_char

    return result


test_cases = int(input())
for tc in range(test_cases):
    result_txt = "Case #" + str(tc+1) + ": "
    print(result_txt, revenge_of_pancakes(input()),sep="")
