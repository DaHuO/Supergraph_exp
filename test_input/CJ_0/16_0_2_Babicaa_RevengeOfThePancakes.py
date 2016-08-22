import sys

__author__ = 'andrej.babic@ringlspil.com'

with open(sys.argv[1]) as input_file:
    with open(sys.argv[2], "w") as output_file:
        number_of_examples = int(input_file.readline())

        for case_number in xrange(1, number_of_examples+1):
            pancakes_input = input_file.readline().rstrip("\n")
            pancakes_stack = [True if pancake == "+" else False for pancake in pancakes_input[::-1]]

            def get_index_first_wrong_pancake_from_bottom(first_index_to_check):
                for first_index in xrange(first_index_to_check, len(pancakes_stack)):
                    if not pancakes_stack[first_index]:
                        return first_index
                return -1

            def get_number_of_pancakes_to_flip(lowest_index_to_check):
                counter = 0
                for last_index in xrange(len(pancakes_input)-1, lowest_index_to_check-1, -1):
                    if not pancakes_stack[last_index]:
                        return counter
                    counter += 1

                return counter

            def flip_pancakes(number_to_flip):
                flipping_stack = []
                for counter in xrange(number_to_flip):
                    flipping_stack.append(not pancakes_stack.pop())

                pancakes_stack.extend(flipping_stack)

            number_of_flips = 0
            first_index_to_flip = get_index_first_wrong_pancake_from_bottom(0)
            while first_index_to_flip > -1:
                # Make the top of the stack plain.
                pancakes_to_flip = get_number_of_pancakes_to_flip(first_index_to_flip)
                if pancakes_to_flip:
                    number_of_flips += 1
                    flip_pancakes(pancakes_to_flip)

                # Reverse the top of the stack to the happy bottom pancakes.
                flip_pancakes(len(pancakes_stack)-first_index_to_flip)

                # Get the next index of the plain pancake.
                first_index_to_flip = get_index_first_wrong_pancake_from_bottom(first_index_to_flip)

                number_of_flips += 1

            output_file.write("Case #%d: %d\n" % (case_number, number_of_flips))
