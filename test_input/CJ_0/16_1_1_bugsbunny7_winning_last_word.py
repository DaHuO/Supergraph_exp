
def combine(current_word, letter):
    result = []
    for word in current_word:
        result.append(word+letter)
        result.append(letter+word)
    return result

#print combine('C','A') #['CA', 'AC']


def win_last_word(word):
    if len(word) == 1:
        return [word]
    whiteboard = []
    current = [word[0]]
    for i in range(1,len(word)):
        next_word_list = combine(current,word[i])
        for each in next_word_list:
            whiteboard.append(each)
        current = next_word_list
    whiteboard.sort(reverse=True)
    whiteboard.sort(key=len, reverse=True)
    #whiteboard.sort(key=lambda item: (-len(item), item))
    return whiteboard

#print win_last_word('Z')


filename = 'A-last-wordsmall-attempt2.in.txt'
with open(filename, 'r') as file, open('output.txt','w') as output:
    lines = [line for line in file]
    test_cases = int(lines[0])
    for i in range(1, test_cases+1):
        
        line = lines[i].strip()
        if (len(win_last_word(line)) >= 1):
            output.write("Case #%d: %s\n" %(i, win_last_word(line)[0]))
        else:
            output.write("Case #%d: %s\n" %(i, ""))


