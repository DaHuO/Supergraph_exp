import sys

__author__ = 'vandeen'

# Helper Functions
def make_word(word):
    last_word = word[0]
    for i in range(1, len(word)):
        c = word[i]
        if c < last_word[0]:
            last_word = last_word + c
        else:
            last_word = c + last_word
    return last_word


# Main Program
if __name__ == "__main__":
    file = sys.argv[1]

    with open(file) as fh:
        fh.readline()  # Strip first line, don't need it
        case_num = 1
        output = open("output.out", "w")

        for s in fh:
            answer = make_word(s)
            output.write("Case #%d: %s" % (case_num, answer))
            case_num += 1

