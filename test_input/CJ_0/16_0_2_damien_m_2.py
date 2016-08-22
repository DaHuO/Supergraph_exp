def inverse(state):
	return '+' if state == '-' else '-'

def flip(cakes, end):
	flipped = ''.join(reversed([inverse(x) for x in cakes[:end]]))
	result = flipped + cakes[end:]
	assert len(result) == len(cakes)
	#print('flipping', cakes, end, '=>', result)
	return result

def solve(cakes):
	ok_state = '+'*len(cakes)
	states = set([cakes])
	prev_states = set()
	for i in range(100):
		#print()
		#print('STEP #',i)
		if ok_state in states:
			return i
		new_states = set()
		prev_states = prev_states.union(states)
		for state in states:
			for end in range(1, len(state)+1):
				new = flip(state, end)
				if new not in prev_states:
					new_states.add(new)
		#states = new_states - prev_states
		states = new_states
		#print('current', len(states))
		#print('prev', len(prev_states))
		#print('new states not in prev', len(states - prev_states))

#assert solve('--+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+-')

assert flip('--+-', 4) == '+-++'
assert solve('--+-') == 3

assert flip('---+++', 3) == '++++++'
assert flip('-', 1) == '+'

assert solve('-') == 1
assert solve('-+') == 1

T = int(input())
for case in range(1, T+1):
	problem = input()
	print("Case #%i: %s" % (case, solve(problem)))