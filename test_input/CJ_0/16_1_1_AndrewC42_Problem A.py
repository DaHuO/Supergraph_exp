tests = int(raw_input())
for test in range(1, tests+1):
    characters = raw_input().strip()
    final_string = ""
    for character in characters:
        if len(final_string) == 0:
            final_string = character

        elif character >= final_string[0]:
            final_string = character + final_string
        else:
            final_string = final_string + character

    print "Case #{}: {}".format(test, final_string)
