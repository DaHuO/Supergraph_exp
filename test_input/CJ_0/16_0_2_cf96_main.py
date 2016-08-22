import copy

from query_collections import Stream


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

class PancakeStack:

    @staticmethod
    def __flip__(pancake):
        return "+" if pancake is "-" else "-"

    def __init__(self, stack_str):
        self.stack = Stream.of(*stack_str)
        self.stack.reverse()
        self.flip_count = 0

    def flip_at(self, position):
        """
        Flips the stack at position, where position is the pancake index starting from
        the bottom of the stack
        :param position: Zero based index in pancake stack from the bottom
        """
        # front of stack, meaning pancakes from bottom to current index
        front = Stream.of(*self.stack.limit(position))

        # reverse the stack (put pancake in new position) then flip
        back = self.stack.skip(position)
        back.reverse()
        back = back.map(lambda val: PancakeStack.__flip__(val))

        self.stack = Stream.concat(front, back)
        self.flip_count += 1

    def at(self, position):
        return self.stack.__getitem__(position)

    @property
    def front(self):
        return self.stack.__getitem__(self.stack.length()-1)

    def get_flip_count(self):
        return self.flip_count

    def size(self):
        return self.stack.length()

def solve(pancake_stack: str) -> int:
    """
    Solves the pancake problem, as given on 2016 Google Code.

    For each element in the string, and starting at the end of the
    string, we will check if the pancake is happy (1). If not,
    flip all bits in positions preceding it, then continue to the next
    position.

    :param pancake_stack: A string of +'s and -'s representing
    the pancake stack, where + is a 'happy side' pancake, and -
    is a not.

    :return: The minimum number of flips to make the entire
    stack 'happy'.
    """
    stack = PancakeStack(pancake_stack)

    for i in range(stack.size()):
        state = stack.at(i)

        if state is '-':

            # if the top is positive, flip it and all
            # other positives immediately following,
            # otherwise we'll have an endless loop
            if stack.front is '+':
                cur_index = 1
                while stack.at(stack.size() - cur_index - 1) == "+":
                    cur_index+=1
                stack.flip_at(stack.size() - cur_index)
            stack.flip_at(i)

    return stack.get_flip_count()

def main():
    reader = DataReader("data.in")
    cases = reader.lines.skip(1)    # skip the case count, we don't need to read it
    results = cases.map(lambda case: case.strip()).\
        map(lambda case: solve(case))

    reader.report(results)
    reader.done()


if __name__ == "__main__":
    main()
