import sys

def isHappy(state):
	for ch in state:
		if ch == '-':
			return False
	return True

def generate(state):
	new_states = []
	lenOfState = len(state)
	for i in range(1,lenOfState+1):
		new_state = ""
		for j in range(0, i):
			if state[j] == '+':
				new_state = new_state + '-'
			else:
				new_state = new_state + '+'
		new_state = new_state + state[i:lenOfState]
		new_states.append(new_state)

	return new_states

if __name__ == "__main__":
	filename = sys.argv[1]
	f = open(filename, 'r')
	lines = f.readlines()
	T = int(lines[0])
	idx = 0
	for i in range(0,T):
		origin_state = lines[i+1]
		states = set([origin_state])
		level = {origin_state:0}
		queue = [origin_state]
		while len(queue) > 0:
			# print(states)
			next_item = queue.pop()
			# print("%3d: %s" % (idx, next_item))
			idx = idx + 1
			current_level = level[next_item]
			if isHappy(next_item):
				print("Case #%d: %d" % (i+1, current_level))
				break
			new_states = generate(next_item)
			for state in new_states:
				if state not in states:
					states.add(state)
					queue.insert(0, state)
					level[state] = current_level + 1


