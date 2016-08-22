limit_N = 10*10*10*10*10*10

def write_answer(index, answer):
    print("Case #%s: %s" % (index, answer))


HAPPY = 1
BLANK = 0

def make_answer(i, flip_number):
    cur_state = HAPPY
    is_change = False
    before_same = True
    all_happy = False
    before = '+'
    index = 0
    for item in str(i):
        if is_change:
            break

        if index == 0 and item == '+':
            index += 1
            continue
        elif index == 0 and item == '-':
            before = '-'
            cur_state = BLANK
        elif item == '+':
            if before == '+':
                index += 1
                continue
            else:
                is_change = True
        elif item == '-':
            if before == '-':
                index += 1
                continue
            else:
                is_change = True
        index += 1

    if is_change or cur_state == BLANK:
        flip_number += 1
        new_i = ''
        new_index = 0
        i_len = len(str(i))
        if index != i_len or is_change:
            index -= 1

        for item in str(i):
            if new_index != index and item == '+':
                new_index += 1
                new_i += '-'
            elif new_index != index and item == '-':
                new_index += 1
                new_i += '+'
            else:
                new_i += item

        if not is_all_happy(new_i):
            flip_number = make_answer(new_i, flip_number)

    return flip_number


def is_all_happy(i):
    for item in (str(i)):
        if item == '-':
            return False

    return True

def main():
    f = open("B-small-attempt.in")

    lines = f.readlines()
    case = lines[0].rstrip()

    for index in range(1,int(case)+1):
        line = lines[index].rstrip()

        flip_number = 0
        answer = make_answer(line, flip_number)
        write_answer(index, answer)

        index += 1

    f.close()


main()


