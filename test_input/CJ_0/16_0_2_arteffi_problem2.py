from collections import deque

INPUT_PATH = 'input-small.in'

def main():
    test_cases = parse_input(INPUT_PATH)
    solutions = []
    for test_case in test_cases:
        solution = solve(test_case)
        solutions.append(solution)
    output_solutions(solutions)


def parse_input(path):
    with open(path) as f:
        n = int(f.readline())
        lines = f.read().split()
    test_cases = [tuple(bool(char == '+') for char in line)
                  for line in lines]
    assert n == len(test_cases)
    return test_cases


def output_solutions(solutions):
    with open('output', 'w') as f:
        for i, solution in enumerate(solutions, 1):
            f.write('Case #{i}: {result}\n'.format(i=i, result=solution))


def solve(start):
    steps = bfs(start, generate_neighbors, is_goal)
    return steps


def bfs(start, generate_neighbors, is_goal):
    """ Return number of steps to get to the goal
    """
    queue = deque([(start, 0)])
    seen = set([start])
    while True:
        state, steps = queue.popleft()
        if is_goal(state):
            return steps
        for neighbor in generate_neighbors(state):
            if neighbor not in seen:
                queue.append((neighbor, steps+1))
                seen.add(neighbor)


# optimized version, only generate splits on True/False borders
def generate_neighbors(state):
    neighbors = []
    for k in range(1, len(state)+1):
        if k < len(state) and state[k - 1] == state[k]:
            continue
        neighbor = tuple((not face) for face in reversed(state[:k])) + state[k:]
        neighbors.append(neighbor)
    return neighbors


# not optimized version:
#def generate_neighbors(state):
#    neighbors = []
#    for k in range(1, len(state)+1):
#        neighbor = tuple((not face) for face in reversed(state[:k])) + state[k:]
#        neighbors.append(neighbor)
#    return neighbors


def is_goal(state):
    return all(state)


if __name__ == '__main__':
    main()
