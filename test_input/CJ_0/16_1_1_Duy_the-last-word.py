#!python2.7

# Standard libs
import argparse

def get_last_word(letters):
    if not letters:
        return ''

    current_word = ''

    while letters:
        next_letter = letters.pop(0)

        if not current_word:
            current_word = next_letter
            continue

        if next_letter >= current_word[0]:
            current_word = next_letter + current_word
        else:
            current_word += next_letter

    return current_word

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file')
    args = parser.parse_args()

    with open(args.input_file) as f:
        num_cases = f.readline()
        for i, line in enumerate(f, start=1):
            starting_word = line.strip()
            print "Case #%d: %s" % (i, get_last_word(list(starting_word)))

if __name__ == "__main__":
    main()

