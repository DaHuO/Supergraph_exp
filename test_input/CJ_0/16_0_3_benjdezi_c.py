from math import sqrt

samples = []
bases = range(2, 11)

num_samples = int(raw_input())
for i in range(num_samples):
    (n, j) = map(lambda x: int(x.strip()), raw_input().split(' '))
    samples.append((n, j))


def generate_sequences(n):
    if n == 1:
        seqs = [[0], [1]]
    else:
        seqs = []
        for sub_seq in generate_sequences(n - 1):
            seqs.append([0] + sub_seq)
            seqs.append([1] + sub_seq)
    return seqs


def eval_in_base(seq, base):
    l = len(seq)
    v = 0
    for i in range(l):
        n = l - 1 - i
        v += seq[i] * pow(base, n)
    return v


def is_prime_in_base(seq, base):
    return (find_divider(seq, base) is None)


def is_prime(seq):
    for b in bases:
        if is_prime_in_base(seq, b):
            return True
    return False


def find_divider(seq, base):
    v = eval_in_base(seq, base)
    for i in range(2, int(sqrt(v)) + 1):
        d = v / (i * 1.0)
        if int(d) == d:
            return i

for i in range(len(samples)):

    (n, j) = samples[i]
    num_jamcoins = 0
    sequences = generate_sequences(n - 2)

    print "Case #%s: " % (i + 1)
    for seq in sequences:
        seq = [1] + seq + [1]
        if not is_prime(seq):
            num_jamcoins += 1
            print "".join(map(lambda x: str(x), seq)),
            for b in bases:
                print find_divider(seq, b),
            print
        if num_jamcoins == j:
            break
            pass
