
def main(inWord):
    alphabetStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = {}
    for x in range(len(alphabetStr)):
        alphabet[alphabetStr[x]] = x + 1
    
    finalStr = ""
    lastScore = 0
    
    for char in inWord:
        if char not in alphabetStr:
            continue
        if alphabet[char] > lastScore or alphabet[char] == lastScore:
            finalStr = char + finalStr
            lastScore = alphabet[char]
        else:
            finalStr += char
    return finalStr
    
 

def fileHandler(inName):
	returnString = ""
	f = open(inName,'r')
	i = 1
	init = True
	for line in f:
		if init == True:
			init = False
			continue
		returnString += "Case #" + str(i) + ": " + main(line) + "\n"
		i += 1
	f.close()
	w = open('results.txt','w')
	w.write(returnString)
	w.close()
fileHandler('A-large (2).in')