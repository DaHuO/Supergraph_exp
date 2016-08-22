'''
Created on Apr 11, 2015

@author: Ankur Patil
'''
import sys
def main(infile, outfile):
	with open(infile,"rt") as f:
		T = int(f.readline())
		sol = []
		for t in range(1,T+1):
			sol.append("Case #{0}:\n".format(t))
			counter = 0
			strN, strJ = f.readline().split(" ")
			N = int(strN)
			strN = str(N-2)
			J = int(strJ)
			for cnt in range(pow(2,N-2)-1):
				str1 = "1{0:0"+strN+"b}1"
				jamcoin = str1.format(cnt)
				res = jamcoin
				for base in range(2,11):
					num = int(jamcoin,base)
					#print("jamcoin: {0}, num: {1}, base: {2}".format(jamcoin,num,base))
					for i in (2,3,5,7,13,19):
						if num % i == 0:
							res = res + " " + str(i)
							break;
					else:
						#print("{0} not good for base {1}".format(jamcoin,base))
						break;
				else:
					counter = counter + 1
					sol.append("{0}\n".format(res))	
					if(counter == J):
						break;
					continue;
				#print("Next cnt")
				#print("Not good {0}".format(jamcoin))
			else:
				print("PROBLEM!!!")
		print(sol)
	with open(outfile, "wt") as f:
		f.writelines(sol)

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])