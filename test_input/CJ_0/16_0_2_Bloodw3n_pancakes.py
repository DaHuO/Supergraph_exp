class Cake():
    def __init__(self, cake):
        self.cake = cake
        self.binaryCake = self.parser()
        self.amountOfTries = 0
        self.flipper()

    def parser(self):
        binaryCake = []
        for i in self.cake:
            if i == '+':
                binaryCake.append(1)
            else:
                binaryCake.append(0)
        return binaryCake

    def flipper(self):
        smile = False
        sad = False
        j = 0
        for i in self.binaryCake:
            j += 1
            if i is 1:
                if sad:
                    self.flipToOne(j)
                    sad = False
                if j is len(self.binaryCake):
                    return 0
                smile = True
                continue
            if i is 0:
                if not smile:
                    if j is len(self.binaryCake):
                        self.flipToOne(j)
                        return 0
                    sad = True
                    continue
                else:
                    self.flipToZero(j)
                    smile = False
                    sad = True
                    continue
        if sad:
            self.flipToOne(j)

    def flipToZero(self, amount):
        for i in range(amount - 1):
            self.binaryCake[i] = 0
        self.amountOfTries += 1

    def flipToOne(self, amount):
        for i in range(amount):
            self.binaryCake[i] = 1
        self.amountOfTries += 1


def main(t):
    for i in range(1, t + 1):
        if i > 100:
            return 0
        t = input()
        cake = Cake(t)
        print("Case #{}: {}".format(i, cake.amountOfTries))


main(int(input()))
