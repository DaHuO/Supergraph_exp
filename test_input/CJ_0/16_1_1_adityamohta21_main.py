text_file = open("A-small-attempt0.in", "r")
lines = text_file.read()
in_text = lines[1:]
in_text_list = in_text.split('\n')
text_file.close()


def binary(i, decimal):  # convert decimal to binary
    b = 0
    while decimal:
        b += (decimal % 2) * i
        i *= 10
        decimal = int(decimal / 2)
    return b


def generate(ch, S):
    temp = ""
    for i in range(len(S)):
        if ch[i] == '0':
            temp = S[i] + temp
        else:
            temp = temp + S[i]
    return temp


def result(S):

    list_S = []
    length = len(S)

    start = 2 ** length
    end = (2 ** (length + 1)) - 1

    for f in range(start, (start + end)//2 + 1):
        str_f = str(binary(1, f))
        C = str_f[1:]
        list_S.append(generate(C, S))

    sorted_list = sorted(list_S)
    return sorted_list[-1]

input_text = in_text_list[1:]
print(input_text)
for i in range(len(input_text)):
    text_file = open("output.txt", "a")
    text_file.write("Case #")
    text_file.write("%s" %str(i+1))
    text_file.write(": %s" %result(input_text[i]))
    text_file.write('\n')
    text_file.close()