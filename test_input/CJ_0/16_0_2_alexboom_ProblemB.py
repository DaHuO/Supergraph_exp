'''
Created on 9 Apr 2016

@author: boom
'''
from time import sleep

class PancakeStack():
    
    def __init__(self):
        self.stack = ''
        self.flips = 0
        
    def set_stack(self, stack):
        self.stack = stack
        
    def happyfy(self):
        pancakesNr = len(self.stack)
        for i, pancake in enumerate(self.stack):
            if (i+1) < pancakesNr:
                if pancake != self.stack[i+1]:
                    self.set_stack(self.flip(self.stack[:i+1]) + self.stack[-(pancakesNr - (i+1)):])
            elif self.stack[-1] == '-':
                self.set_stack(self.flip(self.stack))
    
    def flip(self, array):
        self.flips = self.flips + 1
        array = array[::-1]
        fliped_array = []
        for i in range(len(array)):
            if array[i] == '+': fliped_array.append('-') 
            else: fliped_array.append('+')
        return ''.join(fliped_array)
            
    def happy_pancakes(self, startStack):
        self.set_stack(startStack)
        happyStack = '+' * len(self.stack)
        while (self.stack != happyStack):
            self.happyfy()
        return self.flips
    
def main():
    
    testFile = 'problemB.txt'
    with open(testFile) as f:
        lineCount = 1
        next(f)
        for line in f:
            stack = PancakeStack()
            currLine = line.rstrip('\n')
            print 'Case #' + str(lineCount) + ': ' + str(stack.happy_pancakes(currLine))
            lineCount = lineCount + 1
            if lineCount > 100 : break

if __name__ == '__main__':
    main()