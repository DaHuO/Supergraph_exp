from base import GoogleJamBaseClass


class C(GoogleJamBaseClass):
    def read_case(self, input_file):
        line = input_file.readline().strip()
        length, cases = line.split(' ')
        return [int(length), int(cases)]

    def solve(self, case):
        length, cases = case
        half_length = int(length/2)
        coins = '\n'
        for i in range(0, cases):
            middle = bin(i)
            middle = middle[2:]
            middle = middle.zfill(half_length - 2)
            middle = '1' + middle + '1'
            coins += (middle + middle)
            for j in range(2, 11):
                divisor = 1 + pow(j, half_length)
                coins += (' ' + str(divisor))
            coins += '\n'
        return coins


C().run('C-large.in')
