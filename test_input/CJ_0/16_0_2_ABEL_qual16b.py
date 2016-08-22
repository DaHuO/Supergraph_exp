def flip_pancake(pancake):
    if pancake == '-':
        return '+'
    else:
        return '-'


def flip_partial_stack(stack, flip_index):
    #print('Flip stack {0} at {1}'.format(stack, flip_index))
    to_flip = stack[:flip_index + 1]
    #print('Stack to flip: {0}'.format(to_flip))
    if len(to_flip) == 1:
        flipped = flip_pancake(to_flip)
    elif len(to_flip) == 2:
        flipped = ''.join([flip_pancake(p) for p in to_flip])
    else:
        flipped = ''.join([flip_pancake(p) for p in to_flip][::-1])
    #print('Flipped stack: {0}, remaining: {1}'.format(flipped, stack[flip_index + 1:]))
    return flipped + stack[flip_index + 1:]


def get_all_flip_states(initial_state):
    states = []
    for i in range(initial_state.rfind('-') + 1):
        states.append(flip_partial_stack(initial_state, i))
    return states


def count_future_flips(state):
    current_facing = state[0]
    flip_count = 0
    for facing in state:
        if facing != current_facing:
            flip_count += 1
            current_facing = facing
    return flip_count


def get_best_flip(initial_state):
    states = get_all_flip_states(initial_state)
    #print('All possible states for {0} are {1}'.format(initial_state, states))
    states.sort(key=lambda s: str(s.rfind('-')) + '.' + str(count_future_flips(s)))
    #print('Ordered states: {0}'.format(states))
    #print('Best next state is {0}'.format(states[0]))
    return states[0]


def calculate_min_flips(initial_state):
    #print('Initial state: {0}'.format(initial_state))
    if all(pancake == '+' for pancake in initial_state):
        return 0
    current_state = initial_state
    continue_flipping = current_state.rfind('-') > -1
    flip_count = 0
    while continue_flipping:
        #print('Current state: [{0}]'.format(current_state))
        current_state = get_best_flip(current_state)
        flip_count += 1
        continue_flipping = current_state.rfind('-') > -1
    #print('Took {0} flips'.format(flip_count))
    return flip_count


def handle_file(infile):
    num_cases = int(infile.readline())
    cases = [case.strip() for case in infile.readlines()]
    answers = []

    for i in range(num_cases):
        #print('Case #{0}'.format(i + 1))
        answers.append(calculate_min_flips(cases[i]))

    for i in range(num_cases):
        print('Case #{0}: {1}'.format(i + 1, answers[i]))


if __name__ == '__main__':
    with open("B-small-attempt3.in", "r") as f:
        handle_file(f)
