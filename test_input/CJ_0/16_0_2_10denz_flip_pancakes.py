def main():
    with open('B-large.in') as data:
        testcases = int(data.readline())
        for i in range(testcases):
            num_flippings = check_flippings(data.readline().strip())
            print('Case #{}: {}'.format(i + 1, num_flippings))


def check_flippings(pancake_stack):
    correct_stack = '+' * len(pancake_stack)
    counter = 0
    while pancake_stack != correct_stack:
        if pancake_stack[0] == '+':
            first_split = pancake_stack.find('+-') + 1
            pancake_stack = '-' * first_split + pancake_stack[first_split:]
            # print(pancake_stack)
        else:
            first_split = pancake_stack.find('-+') + 1
            last_split = pancake_stack.rfind('-')
            inverted_middle = flip_string(
                pancake_stack[first_split:last_split + 1])
            pancake_stack = inverted_middle + '+' * (
                first_split + len(pancake_stack) - last_split - 1)
            # print(pancake_stack)
        counter += 1
    return counter


def flip_string(pancake_stack):
    flipped_pancakes = ['+' if char is '-' else '-' for char in pancake_stack]
    return "".join(flipped_pancakes[::-1])

if __name__ == '__main__':
    main()
