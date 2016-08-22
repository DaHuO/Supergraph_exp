#!/usr/bin/env python
# -*- coding: utf-8 -*-


def SWcompare(seq1, seq2, threshold):
	global match, mismatch, gap
	match = 2
	mismatch = -1
	gap = 0

	rows = len(seq1) + 1
	cols = len(seq2) + 1
	# print seq1
	# print seq2

	got_it,score_matrix, start_pos = create_score_matrix(rows, cols, seq1, seq2)
	if not got_it:
		return False
	seq1_aligned, seq2_aligned = traceback(score_matrix, start_pos, seq1, seq2)
	# print seq1
	# print seq2


	se1 = []
	count = 0
	for i in seq1_aligned:
		if i == '#gap#':
			# count += 1
			continue
		se1.append(i)
	se2 = []
	
	for i in seq2_aligned:
		if i == '#gap#':
			count += 1
		se2.append(i)
	# print 'start'
	# print se1
	# print se2
	# print 'end'
	# print se2
	# print 'start'
	# print se1
	# print se2
	# print seq1
	# print len(se1)
	# print len(seq1)
	# print 'end'
	ratio = float(len(se1) - count)/len(seq1)
	# print ratio
	# print len(seq1)
	# print count
	# print ratio
	if ratio >= threshold:
		# print ratio
		# print 'got it'
		# print se1
		# print se2
		return True
	else:
		return False


def create_score_matrix(rows, cols, seq1, seq2):
	score_matrix = [[0 for col in range(cols)] for row in range(rows)]
	max_score = 0
	max_pos   = None
	got_it = True
	for i in range(1, rows):
		for j in range(1, cols):
			score = calc_score(score_matrix, i, j, seq1, seq2)
			if score > max_score:
				max_score = score
				max_pos   = (i, j)
			score_matrix[i][j] = score
	if max_pos == None:
		got_it = False

	return got_it, score_matrix, max_pos


def calc_score(matrix, x, y, seq1, seq2):
	similarity = match if seq1[x - 1] == seq2[y - 1] else mismatch
	diag_score = matrix[x - 1][y - 1] + similarity
	up_score   = matrix[x - 1][y] + gap
	left_score = matrix[x][y - 1] + gap

	return max(0, diag_score, up_score, left_score)

def traceback(score_matrix, start_pos, seq1, seq2):
	END, DIAG, UP, LEFT = range(4)
	aligned_seq1 = []
	aligned_seq2 = []
	x, y = start_pos
	move = next_move(score_matrix, x, y)
	while move != END:
		if move == DIAG:
			aligned_seq1.append(seq1[x - 1])
			aligned_seq2.append(seq2[y - 1])
			x -= 1
			y -= 1
		elif move == UP:
			aligned_seq1.append(seq1[x - 1])
			aligned_seq2.append('#gap#')
			x -= 1
		else:
			aligned_seq1.append('#gap#')
			aligned_seq2.append(seq2[y - 1])
			y -= 1

		move = next_move(score_matrix, x, y)
	aligned_seq1.append(seq1[x - 1])
	aligned_seq2.append(seq2[y - 1])

	return reversed(aligned_seq1), reversed(aligned_seq2)

def next_move(score_matrix, x, y):
	diag = score_matrix[x - 1][y - 1]
	up   = score_matrix[x - 1][y]
	left = score_matrix[x][y - 1]
	if diag >= up and diag >= left:     # Tie goes to the DIAG move.
		return 1 if diag != 0 else 0    # 1 signals a DIAG move. 0 signals the end.
	elif up > diag and up >= left:      # Tie goes to UP move.
		return 2 if up != 0 else 0      # UP move or end.
	elif left > diag and left > up:
		return 3 if left != 0 else 0    # LEFT move or end.
	else:
	    # Execution should not reach here.
		raise ValueError('invalid move during traceback')


if __name__ == '__main__':
	global match, mismatch, gap
	match = 2
	mismatch = -1
	gap = -1
	seq1 = ['def', 'sorter', '(', 'myArray', ',', 'smallsize', '=', '4', ')', ':']
	seq2 = ['while', 'i', '<', 'len', '(', 'left', ')', 'and', 'j', '<', 'len', '(', 'right', ')', ':']
	x = SWcompare(seq1, seq2)
	print x