import argparse


def compute_min_flips(stack_specification):
    """
    Args:
        stack_specification (str): String containing '+' and '-'

    Returns:
        Number of flips necessary to turn all the -s into +s.

    >>> compute_min_flips('-')
    1
    >>> compute_min_flips('-+')
    1
    >>> compute_min_flips('+-')
    2
    >>> compute_min_flips('+++')
    0
    >>> compute_min_flips('--+-')
    3
    """
    if len(stack_specification) == 0: return 0
    # Starting from the top, keep going down until you encounter a pancake
    # facing a direction differently from the top 1. Flip the current stack.
    # Repeat.
    num_flips = 0
    top_pancake_orientation = stack_specification[0]
    for pancake_orientation in stack_specification[1:]:
        if pancake_orientation != top_pancake_orientation:
            num_flips += 1
            top_pancake_orientation = pancake_orientation
    if top_pancake_orientation != '+':
        num_flips += 1
    return num_flips

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()

    flip_counts = []
    with open(args.input_file) as f:
        next(f)  # Ignore count of test cases.
        for line in f:
            line = line.strip()
            flip_counts.append(compute_min_flips(line))
    with open(args.output_file, 'wb') as f:
        for i, count in enumerate(flip_counts):
            f.write('Case #{}: {}\n'.format(i+1, count))
