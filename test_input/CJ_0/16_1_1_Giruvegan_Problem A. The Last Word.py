__author__ = 'Giruvegan'


def lastWord(case_input):
    word = []
    for letter in case_input:
        if len(word) == 0:
            word.append(letter)
            continue
        if letter >= word[0]:
            word.insert(0, letter)
        else:
            word.append(letter)
    return ''.join(word)


if __name__ == '__main__':

    filepath = 'A-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(1, len(all_input)):
        case_input = all_input[i].replace('\n', '')
        fout.write('case #' + str(i) + ': ' + lastWord(case_input) + '\n')