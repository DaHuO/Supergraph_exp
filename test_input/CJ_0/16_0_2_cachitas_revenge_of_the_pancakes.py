import logging


log = logging.getLogger(__name__)


def prepare_pancakes(pancakes_pile):
    log.info('Pancakes pile: %s' % pancakes_pile)

    maneuvers = 0
    n = len(pancakes_pile)
    ideal_pile = '+' * n

    while pancakes_pile != ideal_pile:
        log.debug('Pancake pile is not ready to serve: %s' % pancakes_pile)

        # Lookup pankace pile from the bottom
        for i, pancake in enumerate(pancakes_pile[::-1]):
            if pancake == '-':
                lowest_incorrect_pancake = n - i - 1
                log.debug('Lowest incorrect pancake index: %d'
                          % lowest_incorrect_pancake)
                break
        else:
            log.info('Serving pancakes. It required %d maneuvers' % maneuvers)
            return maneuvers

        pancakes_pile = _flip_top_pancakes(
            pancakes_pile, lowest_incorrect_pancake)

        maneuvers += 1

    log.info('Serving pancakes. It required %d maneuvers' % maneuvers)
    return maneuvers


def _flip_top_pancakes(pancakes_pile, n):
    top_stack, rest = pancakes_pile[:n+1], pancakes_pile[n+1:]
    log.debug('Flipping first pancakes [%s](%s)' % (top_stack, rest))
    stack_flipped = [_flip(pancake) for pancake in top_stack]
    stack_after_maneuver = ''.join(stack_flipped)
    pancakes_pile = stack_after_maneuver + pancakes_pile[n+1:]
    log.debug('Flipping result: %s' % pancakes_pile)
    return str(pancakes_pile)


def _flip(pancake):
    if pancake == '+':
        return '-'
    elif pancake == '-':
        return '+'
    else:
        raise ValueError(pancake)


if __name__ == '__main__':

    logging.basicConfig(level='INFO')

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        log.info(50 * '-' + ' CASE {:>d}'.format(i))
        S = input()
        print("Case #{}: {}".format(i, prepare_pancakes(S)))
