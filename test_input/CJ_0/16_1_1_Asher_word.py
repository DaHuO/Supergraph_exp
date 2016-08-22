# 7
# CAB
# JAM
# CODE
# ABAAB
# CABCBBABC
# ABCABCABC
# ZXCASDQWE

string = "ABAAB"

def find_string(string):
    result = ""

    for char in string:
        if result == "":
            result = char
            
        elif result[0] <= char:
            result = char + result
        else:
            result += char

    return result


file_name = "A-large"

with open(file_name + ".in", "r") as f:
    lines = f.readlines()[1:]
    
with open(file_name + ".out", "w") as f:
    for i, line in enumerate(lines):
        f.write("Case #{}: {}\n".format(i+1, find_string(line.strip())))
