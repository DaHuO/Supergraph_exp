import sys
import string

fname = sys.argv[1]

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def add_letter(self, c):
        # Add letter to all the leaves
        if self.left == None and self.right == None:
            self.left = Tree()
            self.left.data = c+self.data
            self.right = Tree()
            self.right.data = self.data+c
        else:
            self.left.add_letter(c)
            self.right.add_letter(c)

    def get_words(self, words):
        if self.left == None and self.right == None:
            words.append(self.data)
        else:
            self.left.get_words(words)
            self.right.get_words(words)

with open(fname) as f:
    # T - number of test cases
    T = int(string.split(f.readline())[0])

    for t in range(T):
        # S - string of characters
        S = string.split(f.readline())[0]
        #print "S {}".format(S)

        root = None

        # Add characters
        for c in S:
            if root == None:
                root = Tree()
                root.data = c
            else:
                root.add_letter(c)

        # Print all words
        words = []
        root.get_words(words)
        words.sort()
        last_word = words[-1]
        print "Case #{}: {}".format(t+1, last_word)


