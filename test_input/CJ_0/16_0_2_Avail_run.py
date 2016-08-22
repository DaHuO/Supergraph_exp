import sys


def swap(stack, k):
    k += 1
    s = str(stack[k-1::-1])
    s = s.replace('+', 'x').replace('-', '+').replace('x', '-')
    s + stack[k:]

    print("Swap {}: {} -> {}".format(k, stack, s + stack[k:]))

    return s + stack[k:]



def pancake_master(pancake_stack):
    print("New entry:", pancake_stack)

    swaps = 0
    while '-' in pancake_stack:
        # Ignore bottom happy-sides
        pancake_stack = (pancake_stack.rstrip('+'))

        lb = pancake_stack.find('+') - 1 # count of left blanks
        lh = pancake_stack.find('-') - 1 # count of left happys

        # All  blank
        if '+' not in pancake_stack:
            #print("No plus")
            pancake_stack = swap(pancake_stack, len(pancake_stack)-1)
            swaps += 1
        # Swap all if left end has blanks
        elif lb >= 0:
            print("lb", lb)
            pancake_stack = swap(pancake_stack, len(pancake_stack)-1)
            swaps += 1
            # Swap all happy's till first blank
            # Then swap blank too
        elif lh >= 0:
            print("lh", lh)
            pancake_stack = swap(pancake_stack, lh)
            swaps += 1
            #pancake_stack = swap(pancake_stack, lb)
            #swaps += 1

        if swaps > 500:
            break;


    print("Swap count:", swaps)
    return swaps

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as inf:
    with open(outfile, 'w') as outf:
        test_case = 1
        t = inf.readline()
        for line in inf.readlines():

            swaps = pancake_master(line[:-1]) # rm \n

            if test_case != 1:
                outf.write('\n')

            outf.write("Case #{}: {}".format(test_case, swaps) )
            #else:
            #    outf.write("Case #{}: INSOMNIA".format(test_case) )

            test_case += 1
