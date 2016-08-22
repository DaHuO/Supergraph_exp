PLUS = '+'
MINUS = '-'

def flip(pancake):
    new_pancake = list(pancake[::-1])
    for i in range(len(new_pancake)):
        new_pancake[i] = flip_single(new_pancake[i])
    new_pancake = "".join(new_pancake)
    return new_pancake

def flip_top(pancake, top_num):
    new_pancake = pancake[:top_num]
    new_pancake = flip(new_pancake)
    pancake_postfix = pancake[top_num:]
    new_pancake = "".join(new_pancake) + pancake_postfix
    return new_pancake

def flip_single(pancake_single):
    if PLUS == pancake_single:
        return MINUS
    else:
        return PLUS

def same_from_top(pancake):
    sign = pancake[0]
    for i in range(1, len(pancake)):
        if pancake[i] != sign:
            return i
    return len(pancake)
    
def same_from_bottom(pancake):
    new_pancake = pancake[::-1]
    return same_from_top(new_pancake)

def moves_count(pancake, flipped):
    moves = 0
    while pancake:
        if pancake[-1] == PLUS:
            same_bottom_num = same_from_bottom(pancake)
            pancake = pancake[:len(pancake)-same_bottom_num]
        else:
            same_top_num = same_from_top(pancake)
            new_pancake = flip(pancake)
            newer_pancake = flip_top(pancake, same_top_num)
            moves = moves+1
            if flipped:
                return moves_count(newer_pancake, False)+moves
            return min(moves_count(new_pancake, True)+moves, moves_count(newer_pancake, False)+moves)
    return moves

#+++-+++-
if __name__ == '__main__':
    t = int(raw_input())
    for j in range(1, t+1):
        pancake = raw_input()
        plus_pancake = pancake
        moves = moves_count(plus_pancake, False)
        print('Case #%s: %s' % (str(j), str(moves)))