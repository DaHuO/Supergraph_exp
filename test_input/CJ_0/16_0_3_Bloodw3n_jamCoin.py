from itertools import product
class JamCoin():
    def __init__(self, number, testers, numbers):
        self.number = number
        self.testers = testers

class Jam():
    def __init__(self, n, m):
        self.lengthOfJam = n
        self.amountOfJam = m
        self.dividers = []
        self.jammes = []
        self.jammer()

    def jammer(self):
        for i in product("01", repeat = self.lengthOfJam - 2):
            jam = ['1']
            jam.extend(i)
            jam.append('1')
            self.tester("".join(jam))
            if len(self.jammes) == self.amountOfJam:
                return 1

    def tester(self, number):
        jamCoin = JamCoin(number, [], [])
        for i in range(2, 11):
            isPrime, divider = self.is_prime(int(number, i))
            if isPrime:
                return 1
            jamCoin.testers.append(divider)
        self.jammes.append(jamCoin)

    def is_prime(self, number):
        if number == 2 or number == 3: return True, None
        if number < 2 or number % 2 == 0: return False, 2
        if number < 9: return True, None
        if number % 3 == 0: return False, 3
        r = int(number ** 0.5)
        f = 5
        while f <= r:
            if number % f == 0: return False, f
            if number % (f + 2) == 0: return False, (f + 2)
            f += 6
        return True, None


def main(t):
    n, m = [int(s) for s in input().split(" ")]
    jam = Jam(n, m)
    print("Case #1: ")
    amount = 1
    for jamCoint in jam.jammes:
        if amount > jam.amountOfJam:
            return 0
        print(jamCoint.number + " ", end="")
        for i in jamCoint.testers:
            print("{} ".format(i), end="")
        print()
        amount += 1


main(int(input()))
