"""Round 1A - problem A"""

FILE_BASE = "A-large"


def read_file():
    """reads file into list of puzzles"""
    with open(FILE_BASE + ".in") as file:
        cases = int(file.readline())
        puzzles = []
        for _ in range(cases):
            puzzles.append(file.readline().strip())
        return puzzles


def write_file(results):
    """writes results to file"""
    with open(FILE_BASE + ".out", "w+") as file:
        row = 1
        for result in results:
            file.write("Case #{0}: {1}\n".format(row, result))
            row += 1


def solve(puzzle):
    """solve single puzzle"""
    front_char = puzzle[0]
    last_word = ""
    for c in puzzle:
        if c >= front_char:
            front_char = c
            last_word = c + last_word
        else:
            last_word = last_word + c
    return last_word


print(solve("CAB"))
print(solve("JAM"))
print(solve("CODE"))
print(solve("ABAAB"))
print(solve("CABCBBABC"))
print(solve("ABCABCABC"))
print(solve("ZXCASDQWE"))

PUZZLES = read_file()
RESULTS = [solve(puzzle) for puzzle in PUZZLES]

write_file(RESULTS)

