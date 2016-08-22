def lastWord(word):
    last_word = ''
    for char in word:
        if len(last_word) == 0:
            last_word += char
        else:
            if char < last_word[0]:
                last_word = last_word + char
            else:
                last_word = char + last_word
    return last_word

if __name__ == '__main__':
    T = int(input())
    for case in range(1,T+1):
        word = input()
        print("Case #{0}: {1}".format(case,lastWord(word)))