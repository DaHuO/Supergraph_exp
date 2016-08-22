def findResult(S):
	flips = 0
	cons_bit = S[0] # consecutive bit
	for i in range(len(S)):
		if S[i] != cons_bit:
			flips += 1
			cons_bit = S[i]
	if S[-1] == '-':
		flips += 1
	return flips

with open('B-large.in','r') as fin:
	with open('output.out','w') as fout:
		num = int(fin.readline())
		for i in range(1, num+1):
			S = fin.readline().strip()
			result = findResult(S)
			fout.write('Case #' + str(i) + ': ' + str(result) + '\n')

class Node:
    def __init__(self, data = None, nextNode =  None):
        """ Creates a Node object and initializes
            name and next Node """
        self.data = data
        self.next = nextNode
    
class Stack:
    def __init__(self):
        """ Initialize an empty stack """
        self._top = None
        self._size = 0

    def get_size(self):
        """ Returns size of stack """
        return self._size

    def is_empty( self ):
        """ Checks if stack is empty """
        return self._size == 0

    def push(self, item):
        """ Pushes item on top of stack. """
        self._top = Node(item, self._top)
        self._size += 1

    def pop(self):
        """ Pops and returns top item """
        if self._size > 0:
            removedItem = self._top.data
            self._top = self._top.next
            self._size -= 1
            return removedItem
        return None
        
    def peek( self ):
        """ Return top item of stack """
        if self._size > 0:
            return self._top.data