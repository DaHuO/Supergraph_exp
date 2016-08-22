'''
Created on Apr 16, 2016

@author: Ankur Patil
'''
import sys
def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		for t in range(1,T+1):
			S = f.readline().strip()
			top = S[0]
			ans = top
			for c in S[1:]:
				if top <= c:
					top = c
					ans = c + ans
				else:
					ans = ans + c
						
			sol.append("Case #{0}: {1}\n".format(t,ans))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])