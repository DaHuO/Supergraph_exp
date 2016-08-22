"""
File: A_The_Last_Word.py

Author: Sung Uk Ryu

Solution for Google Code Jam 2016, Round 1A: A. The Last Word
"""

f = open('A-large.in', 'r')
out = open('A-large.out', 'w')
n = int(f.readline())

for i in range(1, n+1):
    S = f.readline()
    R = S[0]
    for j in range(1, len(S)):
        if S[j] < R[0]:
            R = R + S[j]
        else:
            R = S[j] + R
    out.write('Case #{}: {}'.format(i, R))

f.close()
out.close()
