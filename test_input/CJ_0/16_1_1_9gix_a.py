"""
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE

Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE
"""

result_table = {

}

def calculate_last_word(word):
    last_word = ''
    for c in word: 
        if len(last_word) == 0:
            last_word += c
        else:
            a = last_word + c
            b = c + last_word

            if a > b:
                last_word = a
            else:
                last_word = b
    return last_word


def main():
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        last_word = calculate_last_word(s)
        print("Case #{}: {}".format(i, last_word))

if __name__ == '__main__':
    main()