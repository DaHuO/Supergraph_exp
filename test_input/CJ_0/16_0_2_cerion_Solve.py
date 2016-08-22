inputData = [line.rstrip('\n') for line in open('B-small-attempt0.in', 'r')]
outputList = []


def flip_sub_seq(seq, index):
    seq_to_flip = seq[:index]
    fix_seq = seq[index:len(seq)]

    flipped_seq = seq_to_flip[::-1].replace('-', '.').replace('+', '-').replace('.', '+')
    return flipped_seq + fix_seq


def find_shortest_flips(start_seq):
    to_flip = [(0, start_seq)]
    flipped = set()
    while len(to_flip) > 0:
        flips, next_seq = to_flip.pop(0)
        if next_seq in flipped:
            continue
        flipped.add(next_seq)

        if '-' not in next_seq:
                return flips

        flips += 1
        for i in range(len(next_seq)):
            flipped_seq = flip_sub_seq(next_seq, i + 1)
            to_flip.append((flips, flipped_seq))


for c in range(1, int(inputData[0]) + 1):
    start_cake_seq = inputData[c]
    shortest_flips = find_shortest_flips(start_cake_seq)
    outputList.append('Case #' + str(c) + ': ' + str(shortest_flips) + '\n')


with open("B-small-attempt0.out", "w") as fw:
    fw.writelines(outputList)
