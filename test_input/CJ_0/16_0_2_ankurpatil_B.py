'''
Created on Apr 11, 2015

@author: Ankur Patil
'''
import sys
def rev(char):
	if char == '+':
		return '-';
	else:
		return '+';

def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		for t in range(1,T+1):
			ans = 0
			init = f.readline()[:-1]
			current = init
			done = "+"*len(init)
			#print("init: {0}  done: {1}".format(init, done))
			while current != done:
				top = current[0]
				cnt = 1
				for l in current[1:]:
					if l != top:
						break;
					else:
						cnt = cnt + 1
				current = rev(top)*cnt + current[cnt:]
				ans = ans + 1
				#print("current: {0}".format(current))
			sol.append("Case #{0}: {1}\n".format(t,ans))
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])