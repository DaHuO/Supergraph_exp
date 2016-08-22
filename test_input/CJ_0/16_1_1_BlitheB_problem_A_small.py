def the_last_word(s):
    result = ""
    first_char = "@"

    for c in s:
        if c >= first_char:
            first_char = c
            result = first_char + result
        else:
            result = result + c
    return result


test_cases = int(input())
for tc in range(test_cases):
    result_txt = "Case #" + str(tc+1) + ": "
    print(result_txt, the_last_word(input()),sep="")
