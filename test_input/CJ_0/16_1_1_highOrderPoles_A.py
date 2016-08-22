import numpy as np

class A:
    def readWord(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            n = raw_input()  # read a list of integers, 2 in this case
            stack = [c for c in n]
            self.cases.append(stack)

    def printOne(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.readWord()
        self.results = self.process(self.cases)
        self.printOne(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.calculate(n))

        return results

    def calculate(self, wordList):
        start = wordList[0]
        progress = [start]

        for i in range(1, len(wordList), 1):
            letter = wordList[i]
            if progress[0] > letter:
                progress.extend(letter)
            else:
                newWords = [letter]
                newWords.extend(progress)
                progress = newWords

        result = "".join(progress)

        return result

def main():
    q1 = A()
    q1.run()


if  __name__ =='__main__':
    main()