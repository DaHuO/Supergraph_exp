def flips(seq):
	i = len(seq) - 1
	flips = 0

	if seq[i] == '-':
		flips = flips + 1

	while i > 0:
		if seq[i] != seq[i-1]:
			flips = flips + 1
		i = i-1

	return flips

filename = 'B-large'
with open(filename + '.in') as f_in:
	trials = int(f_in.readline())
	seqs = f_in.read().splitlines()
	
with open(filename + '.out', 'w') as f_out:
	for i in range(trials):
		seq = seqs[i]
		f = flips(seq)
		#print seq, len(seq), f
		f_out.write('Case #' + str(i+1) + ': ' + str(f) + '\n')

