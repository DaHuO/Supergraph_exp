import sys

sys.stdout = open('ans.out', 'w')

def findNumFlips(stack):
    flips = 0;

    while(all_happy(stack)) :
        find_switch_idx = stack.index('-') + 1
        if '-+'in stack:
            find_switch_idx = stack.index('-+') + 1
        if '+-' in stack:
            find_switch_idx = min(find_switch_idx, stack.index('+-') + 1)
        if not '+' in stack:
            return flips + 1
        stack = flip(stack, find_switch_idx)
        flips += 1
        # print "Stack:", stack, "Index: ", find_switch_idx, "\nflips", flips
    return flips

def flip(stack, idx):
    sub_stack = ''.join(map(switch, stack[:idx:][::-1]))
    return sub_stack + stack[idx::]

def switch(elm):
    return '+' if elm is '-' else '-'

def all_happy(stack):
    return '-' in stack

with open('input.in') as f:
    for idx, stack in enumerate(f):
        if not idx:
            continue;
        # print "\norig_stack: ", stack
        print 'Case #%s: %d' %(idx, findNumFlips(stack))
