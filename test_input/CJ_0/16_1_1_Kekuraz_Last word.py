def produce(word):
    "given a word, produce the 'last word'"
    string = word[0]
    if len(word) > 1:
        rest = word[1:]
        for letter in rest:
            if letter >= string[0]:
                string = letter + string
            else:
                string = string + letter
    return string

def last_word(file):
    L = [line.strip() for line in open(file, "r")]
    words = L[1: int(L[0])+1]
    rstring = ""
    for i in range(len(words)):
        word = words[i]
        case = i+1
        last = produce(word)
        rstring += "Case #{0}: {1}\n".format(case, last)
    return rstring

if __name__ == "__main__":
    file = "A-large.in"
    print(last_word(file))

