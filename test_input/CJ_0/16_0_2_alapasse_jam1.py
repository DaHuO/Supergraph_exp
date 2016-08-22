def groupe_moins(mot):
	res = 0
	precedent = 0
	for signe in mot:
		if signe == '-':
			if precedent == 0:
				res += 1
				precedent = 1
		else:
			precedent = 0
	return res

def pancakes(L):
	if L[0][0]=='+':
		return str(2*groupe_moins(L[0]))
	else:
		return (str(2*groupe_moins(L[0])-1))





def solution_jam1():
	source = open("D:/Google/QualifJamCode16/B-large.in","r")
	output = open("D:/Google/QualifJamCode16/jam2Large.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split()
		output.write('Case #'+str(i+1)+': '+pancakes(liste)+'\n')
	output.close()
	source.close()

solution_jam1()