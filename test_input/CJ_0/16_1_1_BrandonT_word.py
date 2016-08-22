last_word = [];
word = []

def start (input_word):
    global word
    global last_word
    word = list(input_word)
    word.reverse()
    last_word.append(word.pop())
    word_count = len(word)
    for i in range(0, word_count):
        char = word.pop()
        if char >= last_word[0]:
            last_word = [char] + last_word
        elif char < last_word[0]:
            last_word.append(char)
            
    return ''.join(last_word)

def reset():
    global last_word
    last_word = []
    word = []
    
infile = open('A-large.in','r')
cases = int(infile.readline())

count = 1

outfile = open("A-large.out", "w")
for case in range(1, cases + 1):
    word = str(infile.readline())
    outfile.write("Case #" + str(case) + ": " + start(word))
    reset()
    
outfile.close()
