"""Qualification round - problem A"""

FILE_BASE = "B-large"


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
    current_char = puzzle[0]
    flips = 0
    for c in puzzle + "+":
        if c != current_char:
            current_char = c
            flips += 1
    return flips


print(solve("-"))
print(solve("-+"))
print(solve("+-"))
print(solve("+++"))
print(solve("--+-"))

PUZZLES = read_file()
RESULTS = [solve(puzzle) for puzzle in PUZZLES]

write_file(RESULTS)

