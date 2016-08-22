def last_word(s):
    result = s[0]
    for c in s[1:]:
        if c >= result[0]:
            result = c + result
        else:
            result += c
    return result


if __name__ == '__main__':
    f = open('A-large.in')
    f1 = open('out.txt', 'wb')
    T = f.readline().strip()
    case = 1
    for line in f.readlines():
        # print case
        s = line.strip()
        f1.write('Case #' + str(case) + ': ' + last_word(s) + '\n')
        case += 1

    f.close()
    f1.close()
    # s = 'ZAYBXCWDUE'
    # print last_word(s)
