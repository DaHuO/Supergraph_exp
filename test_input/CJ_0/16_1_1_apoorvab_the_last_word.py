__author__ = 'apoorvab'

# Google Code Jam Round 1A - The Last Word

def get_parsed_line():
    return list(map(int, input().split()))


def get_case():
    return input()


if __name__ == '__main__':
    num_cases = get_parsed_line()[0]


    for case_num in range(0, num_cases):

        word = get_case()
        last_word = word[0]

        for letter in word[1:]:

            if letter >= last_word[0]:
                last_word = letter + last_word
            else:
                last_word = last_word + letter

        print("Case #{}: {}".format(case_num + 1, last_word))


