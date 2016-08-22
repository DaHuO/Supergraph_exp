
samples = []
num_samples = int(raw_input())
for i in range(num_samples):
    samples.append(list(raw_input().strip()))

for i in range(num_samples):

    l = samples[i]
    n = len(l)
    last_word = []

    for j in range(n):
        if j == 0:
            last_word.append(l[j])
        elif l[j] >= last_word[0]:
            last_word = [l[j]] + last_word
        else:
            last_word.append(l[j])

    last_word = "".join(last_word)

    print "Case #%s: %s" % (i + 1, last_word)
