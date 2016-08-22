#!/usr/bin/python

def flip (p_list, index):
	for i in range(index+1):
		if p_list[i] == '-':
			p_list[i] = '+'
		else:
			p_list[i] = '-'
		return p_list	

if __name__=='__main__':
	t = int(raw_input())
	for i in xrange(t):
		p_str = raw_input()
		p_list = list(p_str)
		numb_p = len(p_list)
		flip_count = 0
		for p_i in range(numb_p):
			curr_p = p_list[p_i]
			if (p_i+1 != numb_p):
				next_p = p_list[p_i+1]
				if (curr_p != next_p):
					p_list = flip(p_list, p_i)
					flip_count += 1
			else:
				if curr_p == '-':
					p_list = flip(p_list, p_i)
					flip_count += 1
			
		print 'Case #'+str(i+1)+': '+str(flip_count)

			
			
