import sys

class GetOutOfLoop(Exception):
    pass

def func(input_string):
    input_array = list(input_string)
    iter_in = iter(input_array)
    output_array = [iter_in.next()]
    for char in iter_in:
        if ord(char) >= ord(output_array[0]):
            output_array.insert(0, char)
        else:
            output_array.append(char)
    return ''.join(output_array)
    
def format_output(case_num, val):
    return ("Case #{case_num}: {val}\n".format(case_num=case_num, val=val))

def parse_input(io):
    # Dump first line
    io.readline()

    while True:
        try:
            foo = io.readline()
        except:
            io.close()
            break
        else:
            try:
                val = foo.strip() 
                if val: 
                    yield val
                else:
                    break
            except ValueError as e:
                break

def run(io):
    all_output = []
    for index, line in enumerate(parse_input(io)):
        val = func(line)
        output = format_output(index+1, val)
        all_output.append(output)
    return ''.join(all_output).strip()

def main():
    all_output = run(open(sys.argv[1], 'r'))
    print all_output,

if __name__ == "__main__":
    main()
