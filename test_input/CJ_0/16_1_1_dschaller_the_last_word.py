import string

class TheLastWord(object):
    def __init__(self):
        self.alphabet = list(string.ascii_uppercase)
        self.built_word = None

    def analyze(self, S):
        for character in S:
            self.find_last_alphabetical_word_permutation(character)
        return self.built_word

    def find_last_alphabetical_word_permutation(self, character):
        if not self.built_word:
            self.built_word = character
            return
        if self.alphabet.index(character) < self.alphabet.index(self.built_word[0]):
            self.built_word = '{}{}'.format(self.built_word, character)
        else:
            self.built_word = '{}{}'.format(character, self.built_word)


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = str(raw_input())
        result = TheLastWord().analyze(n)
        print "Case #{}: {}".format(i, result)
