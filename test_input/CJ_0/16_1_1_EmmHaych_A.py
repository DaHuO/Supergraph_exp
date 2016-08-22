import sys

input_file = None
output_file = None

def input_read():
    if(input_file):
        return input_file.readline()
    else:
        return input()
def print_output(s):
    print(s)
    if(output_file):
        output_file.write(s + '\n')
def arg_config():
    global input_file
    global output_file
    if(len(sys.argv) > 1):
        input_file = open('inputs/' + sys.argv[1], 'r')
        if(len(sys.argv) > 2):
            output_file = open('outputs/' + sys.argv[2], 'w')

def main():
    T = int(input_read()) # number of test cases
    for t in range(1, T + 1):
        result = ''
        word = input_read().rstrip()
        for char in word:
            if(result == ''):
                result = char
                continue
            if(ord(char) >= ord(result[0])):
                result = char + result
            else:
                result += char
            
        
        print_output('Case #' + str(t) + ': ' + result)

arg_config()
main()