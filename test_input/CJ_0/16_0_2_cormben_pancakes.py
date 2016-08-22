def _strip_data(data):
    return [x.strip() for x in data.readlines()[1:]]


def _write_output(completed_data, out_file):
    out_lines = ['Case #{}: {}\n'.format(i+1, line) for i, line in enumerate(completed_data)]
    out_file.writelines(out_lines)


def coding_challenge_specific_io(challenge_function):
    with open('input') as in_file:
        parsed_data = _parse_data(_strip_data(in_file))
        completed_data = [challenge_function(data) for data in parsed_data]
    with open('output', 'w') as out_file:
        _write_output(completed_data, out_file)


def _parse_data(in_lines):
    return in_lines


def flipper(pancakes):
    cur = []
    move_count = 0
    while not all([x == '+' for x in pancakes]):
        cur = []
        in_sad_stack = False
        for x in pancakes:
            cur.append(x)
            if not in_sad_stack:
                if x == '-':
                    in_sad_stack = True
            else:
                if x == '+':
                    # then trim that last + off, we don't want it
                    cur = cur[:-1]
                    break
        move_count += 1
        if '+' in cur:
            move_count += 1
        pancakes = '+'*len(cur) + pancakes[len(cur):]
    return move_count


if __name__ == '__main__':
    coding_challenge_specific_io(flipper)
