#!/usr/bin/python3
nr_of_tasks = int(input())



for i in range(1,nr_of_tasks+1):
    last_char = ""
    first_char = ""
    result = []
    row = input()
    for character in row:
        if character >= first_char:
            result.insert(0, character)
            first_char = character
        else:
            result.append(character)
            last_char = character
    print("Case #{task}: {result}".format(task=i,
                                 result="".join(result)))
