from base import GoogleJamBaseClass


class B(GoogleJamBaseClass):
    def read_case(self, input_file):
        return input_file.readline().strip()

    def solve(self, case):
        smile = []
        for ch in case:
            if ch == '+':
                value = 1
            else:
                value = 0
            smile = [value] + smile
        search = 0
        result = 0
        for val in smile:
            if val == search:
                result += 1
                search = 1 - search
        return result


B().run('B-large.in')
