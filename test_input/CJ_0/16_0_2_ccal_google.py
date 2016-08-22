def crearLista(stack):
	lStack = []
	for ch in stack[:-1]:
		lStack.append(ch)
	return lStack;

def girarLista(lStack):
	indicesAGirar = 0
	for i in range(len(lStack)):
		if lStack[i] == '-':
			indicesAGirar = i+1
	
	for i in range(indicesAGirar):
		if lStack[i] == '-':
			lStack[i] = '+'
		else:
			lStack[i] = '-'

def continuar(lStack):
	for i in range(len(lStack)):
		if lStack[i] == '-':
			return True
	return False

fichero = open('input','r')
numcases = int(fichero.readline());
for i in range(numcases):
	stack = fichero.readline();	
	numGiros = 0
	lStack = crearLista(stack)
	
	while continuar(lStack):
		numGiros += 1
		girarLista(lStack);	

	print 'Case #'+str(i+1)+': ' + str(numGiros)
