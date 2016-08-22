def function(liste):
	mot = liste[0]
	result = mot[0]
	compteur = 0
	for c in mot:
		if compteur > 0:
			if ord(c) >= ord(result[0]):
				result = c + result
			else:
				result = result + c
		compteur += 1
	return result


def solution_jam1():
	source = open("D:/Google/QualifJamCode16/A-large.in","r")
	output = open("D:/Google/QualifJamCode16/solution1.txt","w")
	liste = source.readline()
	liste = liste.split('\n')
	for i in range(int(liste[0])):
		liste = source.readline()
		liste = liste.split()
		output.write('Case #'+str(i+1)+': '+function(liste)+'\n')
	output.close()
	source.close()

solution_jam1()