def find_last_word(file_name):
    read_file_name = file_name
    write_file_name = file_name + ' - answer.txt'
    
    read_file = open(read_file_name)
    write_file = open(write_file_name, "w")
    
    cases = int(read_file.readline())
    
    current_case = 1
    
    while current_case <= cases:
        word = read_file.readline().rstrip()
        output = "Case #{0}: {1}\n".format(current_case, last_word(word))
        write_file.write(output)
        current_case += 1
        

def last_word(word):
    result = first_letter = word[0]
    
    for char in word[1:]:
        if char < first_letter:
            result = result + char
        else:
            result = char + result
            first_letter = char
    
    return result

#def last_word(word):
    #if len(word) == 1:
        #return word
    #else:
        #prev_last_word = last_word(word[:-1])
        #last_letter = word[-1]
        #if prev_last_word[0] < last_letter:
            #return last_letter + prev_last_word
        #else:
            #return prev_last_word + last_letter

if __name__ == "__main__":
    find_last_word("test.txt")
    #find_last_word("A-small-attempt0.in")
    find_last_word("A-large.in")