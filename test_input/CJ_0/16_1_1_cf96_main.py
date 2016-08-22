from query_collections import Stream
from collections import deque

class DataReader(object):
    working_file = None
    __lines__ = None

    def __init__(self, file_name):
        self.working_file = open(file_name, "r")
        self.out_file = open("data.out", "w")

    @property
    def lines(self):
        if self.__lines__ is None:
            self.__lines__ = Stream.of(*self.working_file.readlines())
        return self.__lines__

    def __report__(self, result):
        self.out_file.writelines(result + "\n")

    def report(self, results: list):
        case_no = 1
        for case in results:
            self.__report__("Case #%d: %s" % (case_no, str(case)))
            case_no += 1

    def done(self):
        self.working_file.close()
        self.out_file.close()

def solve(case: str):
    letters = deque(case)
    result = deque()
    result.append(letters.popleft())

    if case.__len__() > 1:
        while letters:
            value = letters.popleft()
            if value >= result[0]:
                result.appendleft(value)
            else:
                result.append(value)

    return ''.join(result)


def main():
    reader = DataReader("data.in")
    cases = reader.lines.skip(1)  # skip the case count, we don't need to read it
    results = cases.map(lambda case: case.strip()). \
        map(lambda case: solve(case))
    reader.report(results)
    reader.done()


if __name__ == "__main__":
    main()
