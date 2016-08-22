#!/usr/bin/python3

def solve(input_id):
    letters = input()

    output = letters[0]
    letters = letters[1:]

    for letter in letters:
        if letter >= output[0]:
            output = letter + output
        else:
            output = output + letter
    print('Case #%d: %s' % (input_id, output))

def main():
    num_inputs = int(input())
    for n in range(1,num_inputs + 1):
        solve(n)

main()
