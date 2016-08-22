import abc


class GoogleJamBaseClass(object):
    def run(self, filename):
        input_file = open(filename, "r")
        output_file = open('outpur.txt', "w")
        number_of_cases = int(input_file.readline())
        for i in range(1, number_of_cases + 1):
            case = self.read_case(input_file)
            solution = self.solve(case)
            output_file.write('Case #' + str(i) + ': ' + str(solution) + '\n')

    @abc.abstractmethod
    def read_case(self, input_file):
        pass

    @abc.abstractmethod
    def solve(self, case):
        pass
