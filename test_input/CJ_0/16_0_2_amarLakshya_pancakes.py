#!/usr/bin/env python


class pancakes():
    def __init__(self):
        self.count = 1;
        self.eff = 0;

    def flip(self,pancake):
        pancake = list(pancake)
        for i in range(len(pancake)):
            if(pancake[i] == "-"):
                pancake[i] = "+"
            elif(pancake[i] == "+"):
                pancake[i] = "-"
        pancake = "".join(pancake)
        return pancake


    def allHappy(self,pancake):
        return '-' not in pancake


    def seeHappy(self,pancakes):
            index = 0
            for pancake in pancakes:
                if(not self.allHappy(pancake)):
                    self.eff = self.eff + 1
                    temp = self.flip(pancakes[:index])
                    pancakes = temp + pancakes[index:];
                if(not self.allHappy(pancakes[0]) and not self.allHappy(pancakes)):
                    if(self.allHappy(self.flip(pancakes))):
                        self.eff = self.eff + 1
                        pancakes = self.flip(pancakes)
                    else:
                        pancakes = self.seeBlank(pancakes)

                if(self.allHappy(pancakes)):
                    return pancakes
                index = index + 1
            return pancakes



    def seeBlank(self,pancakes):
            index = 0

            for pancake in pancakes:
                if(self.allHappy(pancake)):
                    self.eff = self.eff + 1
                    temp = self.flip(pancakes[:index])
                    pancakes = temp + pancakes[index:];


                if(self.allHappy(pancakes[0]) and not self.allHappy(pancakes)):
                    pancakes = self.seeHappy(pancakes);

                if(self.allHappy(pancakes)):
                    return pancakes
                index = index + 1
            return pancakes


    def printHappy(self,pancakes):
        if(self.allHappy(pancakes)):
            print "Case #"+str(self.count)+":\t"+str(self.eff)
            return

    def sort(self):
        stack = []
        newcakes = ""
        #stack = ["-","-+","+-","+++","--+-"]
        stack = [line.rstrip('\n') for line in open('in')]
        stack = stack[1:]
        self.count= 1
        for pancakes in stack:
            self.eff = 0
            newcakes = ""
            if(self.allHappy(self.flip(pancakes)) and len(pancakes) == 1):
                self.eff = self.eff + 1
                newcakes = self.flip(pancakes)

            elif(self.allHappy(self.flip(pancakes))):
                    self.eff = self.eff + 1
                    newcakes = self.flip(pancakes)
            else:
                if(self.allHappy(pancakes)):
                    newcakes = pancakes;
                else:
                    if(not self.allHappy(pancakes[0])):
                        newcakes = self.seeBlank(pancakes)

                    if(self.allHappy(pancakes[0]) and not self.allHappy(pancakes)):

                        newcakes = self.seeHappy(pancakes)


            self.printHappy(newcakes)
            self.count = self.count + 1

cakes = pancakes()


cakes.sort()
